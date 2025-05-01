
from monosearch.ability.llm import silicon_flow


def main():
    query = "内卷"
    user_prompt = f"""
        你是一个锐评高手，擅长根据用户输入进行刻薄的锐评。
        【用户输入】{query}
    """
    result = silicon_flow.chat(user_prompt)
    print(result.choices[0].message.content)
    
    
if __name__ == "__main__":
    main()