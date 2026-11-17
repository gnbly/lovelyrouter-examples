// Call GPT with the official OpenAI Node SDK through Lovely Router, streaming,
// then print the token usage and the request id.
import OpenAI from 'openai';

const MODEL = 'gpt-5.6-luna';

const client = new OpenAI({
  baseURL: 'https://lovelyrouter.com/v1', // the only change from stock OpenAI code
  apiKey: process.env.LOVELY_API_KEY,
});

const { data: stream, response } = await client.chat.completions
  .create({
    model: MODEL,
    messages: [{ role: 'user', content: 'Write a haiku about routers.' }],
    stream: true,
    stream_options: { include_usage: true }, // the last chunk carries usage
  })
  .withResponse();

let usage;
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? '');
  if (chunk.usage) usage = chunk.usage;
}

console.log('\n');
console.log(`model: ${MODEL}`);
console.log(
  `tokens: prompt=${usage?.prompt_tokens} ` +
    `cached=${usage?.prompt_tokens_details?.cached_tokens ?? 0} ` +
    `completion=${usage?.completion_tokens}`,
);
console.log(`request id: ${response.headers.get('x-lovely-request-id')}`);
console.log(
  'cost: the Chat Completions response has no cost field. The charge for this request id ' +
    'is in Logs (https://lovelyrouter.com/app/logs); per-token prices are in GET /v1/models.',
);
