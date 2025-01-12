import json

from openai import OpenAI


def extract_info_from_text(text):
    client = OpenAI(
        api_key="aa-ZAyyQX9y072RyJorOyx1zDtS7dk4MJUiifyEzNmj5xen56tX", base_url="https://api.avalai.ir/v1"
    )

    prompt = f"""لطفاً متن زیر را تحلیل کن و اطلاعات مربوط به ساعت شروع، ساعت پایان، پروژه، موضوع فعالیت و خلاصه فعالیت را استخراج کن. تاریخ‌ها باید به صورت شمسی (مانند 1403/01/01) ارائه شوند. ساعت شروع کاری 08:00 و ساعت پایان 15:00 است. اگر هر یک از این اطلاعات وجود نداشت، مقدار آن را به صورت `null` برگردان. اگر اطلاعات مرتبط دیگری نیز وجود دارد، آن را ذکر کن:
    activity_subject:  موضوع فعالیت هست ماننده جلسه، کدنویسی، پشتیبانی، آموزش
    activity_summary : خلاصه ای از اون موضوع فعالیت اگر گفته شده است 
    date: اگر تاریخ گفته نشده بود تاریخ همان روز را برگردان
    متن: "{text}"

    پاسخ را به صورت JSON برگردان. به عنوان مثال:
            "activities": [
                {{
            "date": "1403/10/17",
                "start_time": "08:00",
                "end_time": "11:00",
                "project": "رهتال",
                "activity_subject": "کدنویسی",
                "activity_summary": "اضافه کردن api هایه مورد نیاز فرانت اند"
            }},
                { {
            "date": "1403/10/17",
                "start_time": "12:00",
                "end_time": "13:00",
                "project": "زروند",
                "activity_subject": "بررسی مستندات",
                "activity_summary": "بررسی و تحلیل مستندات پروژه"
            }},
                {   {
            "date": "1403/10/16",
                "start_time": "08:00",
                "end_time": "15:00",
                "project": "زرآمد",
                "activity_subject": "پشتیبانی",
                "activity_summary": "null"
            }}
            ]
            """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
            "content": "شما یک دستیار هوشمند هستید که اطلاعات مربوط به فعالیت‌های روزانه را استخراج می‌کنید."},
            {"role": "user",
            "content": prompt}
        ]
    )
    return response.choices[0].message.content

text = ("امروز از صبح تا 11 روی پروژه رهتال کار کردم و بعد از ساعت 12 تا 1 روی مستندات پروژه زروند کار کردم. و دیروز "
        "تمام وقت روی زرآمد کار کردم")
info = extract_info_from_text(text)
print("اطلاعات استخراج‌شده:", info)
