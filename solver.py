import g4f

def solve_math(question):
    print(f"\n[جاري البحث في السيرفرات البديلة لحل: {question}...]\n")
    # قائمة بمزودي الخدمة المجانيين والأكثر استقراراً
    providers = [g4f.Provider.Blackbox, g4f.Provider.DuckDuckGo, g4f.Provider.DeepInfra]
    
    for provider in providers:
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4o,
                provider=provider,
                messages=[{"role": "user", "content": "Provide ONLY numerical solution with steps for: " + question}],
            )
            if response:
                return response
        except:
            continue
            
    return "السيرفرات مزدحمة حالياً، يرجى إعادة المحاولة بعد ثوانٍ."

print("النتيجة هي: ", solve_math("5 + 5"))
