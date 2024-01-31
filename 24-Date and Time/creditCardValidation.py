from datetime import*

def validateCard(expDate):
    if expDate > datetime.now().date():
        print("valid")
    else:
        print("Expired")
        
validateCard(date(2024,12,12))