import time
from plyer import notification

if __name__ == "__main__":
    while True:
        """
        notification.notify(
            title= "Drink Water now",
            message= "Water recommendations are different for men and women. Men should aim for 3.7 liters and Women need 2.7 liters daily",
            timeout=10,
            app_icon= "C:\\Users\\hp\\PycharmProjects\\Reminder\\icon.ico"
        )
        """
        notification.notify(
            title="YOU ARE AWESOME",
            message="“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
            timeout=10,
            app_icon="C:\\Users\\hp\\PycharmProjects\\Reminder\\icon2.ico"
        )
        time.sleep(60*20)