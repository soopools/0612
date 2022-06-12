import mydetect
# pip install coolsms_python_sdk
import sendMSG
import image
import time

if __name__ == '__main__':
    source = 'car/download.jpg'
    current_len = image.getCountFromDB()

    while(1):
        print("Server is processing now......")
        if (current_len != image.getCountFromDB()):
            location = image.getImgFromDB()

            detect_flag = False
            for i in range(1, 5):
                image.rotate(source)
                # 장애인차량 판별
                if mydetect.detect(source):
                    detect_flag = True

            if detect_flag:
                print("Disabled parking Correct!!!")
            else:
                print("Illegal parking detected!!!")
                # 경찰한테 메세지 보내기
                sendMSG.sendMessage(source, location)  # <- 이거 돈나갑니다 신중하게 쓰세요

            # show image
            image.showImage(source)

            current_len = image.getCountFromDB()

        time.sleep(10)
