import cv2

from python_tools.utils.DateUtils import DateUtils
from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.FileUtils import FileUtils


def createSaveImgPath(saveBasePath,userName,picName):
    return FileNameUtils.join(saveBasePath,userName,picName)

def video_record_img(saveBasePath,userName):
    """
    摄像头录取图片
    :param savePath:
    :param userName:
    :return:
    """
    fp = FileNameUtils.join(saveBasePath, userName)
    FileUtils.mkdir(fp)
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret_fag,vshow = cap.read()
        cv2.imshow('result',vshow)
        k=cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            sp=createSaveImgPath(saveBasePath,userName,DateUtils.get_date_str("%Y%m%d%H%M%S")+'.jpg')
            cv2.imwrite(sp,vshow)
            print('success to save ' + sp)
        elif k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    bp = '/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/out'
    un = 'asa'
    video_record_img(bp, un)