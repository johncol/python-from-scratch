# echo $OPENAI_API_KEY
# python3 --version
# pip3 install openai

from openai import OpenAI

client = OpenAI()

prompt = "If you had to guess, what's the meaning of life?"
n=3

response = client.chat.completions.create(
  n=n,
  model="gpt-4",
  messages=[
    { "role": "user", "content": prompt }
  ]
)

print(f"The prompt was: {prompt}")
print(f"{n} responses were generated:")

for i, choice in enumerate(response.choices):
  reply = choice.message.content.strip()
  print(f"Reply {i+1}: {reply}")
