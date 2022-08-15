import unittest

from python_tools.face.recognition.record_pic import createSaveImgPath, video_record_img


class TesRecord_Pic(unittest.TestCase):

    def test_coordinateCompare(self):
          self.assertEqual(createSaveImgPath("./","asa","a.jpg"),"./asa/a.jpg")
    def test_video_record_img(self):
        bp='/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/out'
        un='asa'
        video_record_img(bp,un)


if __name__ == '__main__':
    unittest.main()
