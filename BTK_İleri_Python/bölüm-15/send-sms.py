import vonage

client=vonage.Client(key="key bilgisi",secret="secret bilgisi")

sms = vonage.Sms(client)

responseData = sms.send_message({
    "from":"Deneme",
    "to":"+90 0500 000 00",
    "text":"deneme smsi"
})

if responseData["messages"][0]["status"]=="0":
    print("mesajnız gönderildi")
else:
    print(f"hata oluştu",{responseData['messages'[0]['error-text']]})

