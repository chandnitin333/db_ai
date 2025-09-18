# OpenAI Custom Modules Guide

## Table of Contents
1. [Overview](#overview)
2. [Creating Custom Modules](#creating-custom-modules)
3. [Training Modules](#training-modules)
4. [Available Modules & Pricing](#available-modules--pricing)
5. [Implementation Guide](#implementation-guide)
6. [Best Practices](#best-practices)
7. [Code Examples](#code-examples)

## Overview

OpenAI provides several approaches for creating custom AI modules tailored to specific business needs. This guide covers the main methods: Fine-tuning, Custom GPTs, Function Calling, and Assistants API.

## Creating Custom Modules

### 1. Fine-Tuning
Fine-tuning allows you to customize OpenAI models on your specific dataset.

**Use Cases:**
- Domain-specific language understanding
- Consistent output formatting
- Improved performance on specific tasks
- Specialized knowledge integration

**Process:**
1. Prepare training data in JSONL format
2. Upload dataset to OpenAI
3. Create fine-tuning job
4. Monitor training progress
5. Deploy fine-tuned model

### 2. Custom GPTs
Build specialized AI assistants with custom instructions and knowledge.

**Features:**
- Custom instructions and personality
- File uploads for knowledge base
- Integration with external APIs
- Web browsing capabilities
- Code interpreter access

### 3. Function Calling
Enable models to call external functions and APIs.

**Capabilities:**
- Real-time data retrieval
- External system integration
- Dynamic content generation
- Complex workflow automation

### 4. Assistants API
Create AI assistants with persistent conversations and tool usage.

**Features:**
- Persistent threads
- Code interpreter
- File search capabilities
- Function calling
- Stateful conversations

## Training Modules

### Data Preparation

#### Fine-Tuning Data Format
```json
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}, {"role": "assistant", "content": "The capital of France is Paris."}]}
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 2+2?"}, {"role": "assistant", "content": "2+2 equals 4."}]}
```

#### Data Quality Guidelines
- **Minimum dataset size:** 10-50 examples (recommended: 100-1000)
- **Consistent formatting:** Ensure uniform structure
- **Diverse examples:** Cover various use cases
- **Quality over quantity:** High-quality examples are crucial
- **Balanced dataset:** Avoid bias in training data

### Training Process

#### 1. Data Validation
```bash
# Validate training data
openai tools fine_tunes.prepare_data -f training_data.jsonl
```

#### 2. Upload Training File
```python
import openai

# Upload training file
training_file = openai.File.create(
    file=open("training_data.jsonl", "rb"),
    purpose='fine-tune'
)
```

#### 3. Create Fine-Tuning Job
```python
# Create fine-tuning job
fine_tune = openai.FineTuningJob.create(
    training_file=training_file.id,
    model="gpt-3.5-turbo",
    hyperparameters={
        "n_epochs": 3,
        "batch_size": 1,
        "learning_rate_multiplier": 2
    }
)
```

#### 4. Monitor Training
```python
# Check fine-tuning status
status = openai.FineTuningJob.retrieve(fine_tune.id)
print(f"Status: {status.status}")
```

## Available Modules & Pricing

### Model Options

#### GPT-4 Models
| Model | Input Price (per 1K tokens) | Output Price (per 1K tokens) | Context Window |
|-------|----------------------------|-------------------------------|----------------|
| GPT-4 | $0.03 | $0.06 | 8,192 tokens |
| GPT-4-32k | $0.06 | $0.12 | 32,768 tokens |
| GPT-4 Turbo | $0.01 | $0.03 | 128,000 tokens |

#### GPT-3.5 Models
| Model | Input Price (per 1K tokens) | Output Price (per 1K tokens) | Context Window |
|-------|----------------------------|-------------------------------|----------------|
| GPT-3.5 Turbo | $0.0015 | $0.002 | 4,096 tokens |
| GPT-3.5 Turbo 16k | $0.003 | $0.004 | 16,384 tokens |

#### Fine-Tuning Costs
| Model | Training Price (per 1K tokens) | Usage Price Multiplier |
|-------|--------------------------------|----------------------|
| GPT-3.5 Turbo | $0.008 | 8x base model price |
| Davinci-002 | $0.006 | 12x base model price |
| Babbage-002 | $0.0004 | 16x base model price |

### Additional Services
- **Embeddings (ada-002):** $0.0001 per 1K tokens
- **Whisper (Audio):** $0.006 per minute
- **DALL-E 3:** $0.04-$0.08 per image
- **Function Calling:** No additional cost

## Implementation Guide

### 1. Environment Setup

```bash
# Install OpenAI SDK
npm install openai
# or
pip install openai
```

### 2. Basic Configuration

```javascript
// Node.js/TypeScript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
```

```python
# Python
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
```

### 3. Integration with Frequence Platform

#### PHP Integration (CodeIgniter)
```php
<?php
// application/libraries/Openai_lib.php

class Openai_lib {
    private $api_key;
    private $base_url = 'https://api.openai.com/v1/';

    public function __construct() {
        $this->api_key = $this->CI->config->item('openai_api_key');
    }

    public function chat_completion($messages, $model = 'gpt-3.5-turbo') {
        $data = [
            'model' => $model,
            'messages' => $messages,
            'temperature' => 0.7
        ];

        return $this->make_request('chat/completions', $data);
    }

    private function make_request($endpoint, $data) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $this->base_url . $endpoint);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Authorization: Bearer ' . $this->api_key,
            'Content-Type: application/json'
        ]);

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode($response, true);
    }
}
```

#### Angular Service Integration
```typescript
// angular/src/app/shared/services/openai.service.ts

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OpenaiService {
  private apiUrl = '/api/openai'; // Proxy through backend

  constructor(private http: HttpClient) {}

  generateChatCompletion(messages: any[], model: string = 'gpt-3.5-turbo'): Observable<any> {
    const payload = {
      model,
      messages,
      temperature: 0.7
    };

    return this.http.post(`${this.apiUrl}/chat/completions`, payload);
  }

  generateSmartProposal(proposalData: any): Observable<any> {
    const messages = [
      {
        role: 'system',
        content: 'You are an expert advertising proposal generator. Create detailed, professional proposals based on the provided data.'
      },
      {
        role: 'user',
        content: `Generate a proposal for: ${JSON.stringify(proposalData)}`
      }
    ];

    return this.generateChatCompletion(messages);
  }
}
```

### 4. Custom Module Examples

#### Campaign Optimization Module
```python
class CampaignOptimizerModule:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def optimize_campaign(self, campaign_data):
        prompt = f"""
        Analyze this campaign data and provide optimization recommendations:

        Campaign: {campaign_data['name']}
        Budget: ${campaign_data['budget']}
        Target Audience: {campaign_data['audience']}
        Current CTR: {campaign_data['ctr']}%
        Current CPC: ${campaign_data['cpc']}

        Provide specific, actionable recommendations for improvement.
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert digital marketing strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    def generate_ad_copy(self, product_info, target_audience):
        prompt = f"""
        Create compelling ad copy for:
        Product: {product_info['name']}
        Features: {', '.join(product_info['features'])}
        Target: {target_audience}

        Generate 3 headline options and 2 description options.
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )

        return response.choices[0].message.content
```

#### Proposal Generator Module
```typescript
// Angular Component for Smart Proposal Generation
export class SmartProposalComponent {
  constructor(private openaiService: OpenaiService) {}

  generateProposal(clientData: any, campaignRequirements: any) {
    const systemPrompt = `
      You are an expert advertising strategist creating proposals for digital campaigns.
      Always include: objectives, target audience, recommended channels, budget allocation, timeline, and KPIs.
      Format responses in professional business language suitable for client presentations.
    `;

    const userPrompt = `
      Create a comprehensive advertising proposal for:

      Client: ${clientData.company_name}
      Industry: ${clientData.industry}
      Budget: $${campaignRequirements.budget}
      Goals: ${campaignRequirements.objectives.join(', ')}
      Timeline: ${campaignRequirements.duration} months
      Target Audience: ${campaignRequirements.target_audience}

      Include specific channel recommendations with budget allocation percentages.
    `;

    return this.openaiService.generateChatCompletion([
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userPrompt }
    ]).subscribe(response => {
      // Process and display the generated proposal
      this.handleProposalResponse(response);
    });
  }
}
```

## Best Practices

### 1. Prompt Engineering
- **Be specific:** Clear, detailed instructions yield better results
- **Use examples:** Provide sample inputs and expected outputs
- **Set context:** Define the AI's role and expertise level
- **Control output:** Specify format, length, and style requirements

### 2. Error Handling
```typescript
async function safeOpenAICall(prompt: string): Promise<string> {
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: prompt }],
      max_tokens: 1000,
      timeout: 30000 // 30 second timeout
    });

    return response.choices[0].message.content;
  } catch (error) {
    if (error.status === 429) {
      // Rate limit - implement retry with backoff
      await delay(1000);
      return safeOpenAICall(prompt);
    } else if (error.status === 401) {
      throw new Error('Invalid API key');
    } else {
      console.error('OpenAI API error:', error);
      return 'Error generating response. Please try again.';
    }
  }
}
```

### 3. Cost Optimization
- **Use appropriate models:** GPT-3.5 for simpler tasks, GPT-4 for complex reasoning
- **Implement caching:** Store common responses to reduce API calls
- **Optimize prompts:** Shorter prompts reduce token usage
- **Batch requests:** Group multiple requests when possible
- **Set token limits:** Use max_tokens to control costs

### 4. Security Considerations
- **API key protection:** Store keys securely, never in client-side code
- **Input validation:** Sanitize all user inputs before sending to OpenAI
- **Rate limiting:** Implement proper rate limiting to prevent abuse
- **Content filtering:** Monitor outputs for inappropriate content
- **Data privacy:** Ensure sensitive data is handled according to compliance requirements

## Code Examples

### Complete Integration Example

```php
<?php
// application/controllers/Ai_controller.php

class Ai_controller extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->load->library('openai_lib');
        $this->load->model('proposal_model');
    }

    public function generate_smart_proposal() {
        $proposal_id = $this->input->post('proposal_id');
        $proposal_data = $this->proposal_model->get_proposal($proposal_id);

        $messages = [
            [
                'role' => 'system',
                'content' => 'You are an expert advertising strategist creating detailed campaign proposals.'
            ],
            [
                'role' => 'user',
                'content' => $this->build_proposal_prompt($proposal_data)
            ]
        ];

        $response = $this->openai_lib->chat_completion($messages, 'gpt-4');

        if ($response && isset($response['choices'][0]['message']['content'])) {
            $generated_content = $response['choices'][0]['message']['content'];

            // Save generated proposal
            $this->proposal_model->update_proposal($proposal_id, [
                'ai_generated_content' => $generated_content,
                'generation_timestamp' => date('Y-m-d H:i:s')
            ]);

            $this->output
                ->set_content_type('application/json')
                ->set_output(json_encode([
                    'success' => true,
                    'content' => $generated_content
                ]));
        } else {
            $this->output
                ->set_content_type('application/json')
                ->set_status_header(500)
                ->set_output(json_encode([
                    'success' => false,
                    'error' => 'Failed to generate proposal'
                ]));
        }
    }

    private function build_proposal_prompt($proposal_data) {
        return "
            Generate a comprehensive advertising proposal with the following details:

            Client: {$proposal_data['client_name']}
            Industry: {$proposal_data['industry']}
            Budget: ${$proposal_data['budget']}
            Campaign Duration: {$proposal_data['duration']} months
            Target Audience: {$proposal_data['target_audience']}
            Campaign Objectives: {$proposal_data['objectives']}

            Include:
            1. Executive Summary
            2. Campaign Strategy
            3. Channel Recommendations with budget allocation
            4. Timeline and Milestones
            5. Expected KPIs and ROI
            6. Next Steps

            Format as professional business proposal suitable for client presentation.
        ";
    }
}
```

This comprehensive guide provides everything needed to implement custom OpenAI modules within the Frequence Platform, from basic setup to advanced integration patterns.