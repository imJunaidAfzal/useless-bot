from openai import OpenAI

client = OpenAI(api_key="YOUR_OPEN_AI_KEY_HERE")



def openai_bot(message, chat_history):
    print(f"Chat His: {chat_history}")
    system_prompt = open("system_prompt.txt", "r").read()
    max_tokens = 200
    temperature = 0.7

    msgs = [{"role": "system", "content": system_prompt}]
    for user_m, assis in chat_history:
        msgs.append({"role": "user", "content": user_m})
        msgs.append({"role": "assistant", "content": assis})
    msgs.append({"role": "user", "content": message})
    response = client.chat.completions.create(
    model="gpt-4",
    messages=msgs,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    )

    print(response.choices[0].message.content)

    chat_history.append((message, response.choices[0].message.content))

    return "", chat_history
