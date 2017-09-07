import unittest
import barcodeVideo as bv
import numpy as np
import cv2
import os

class TestHelpers(unittest.TestCase):

	def test_avg_row(self):
		frame = cv2.imread('testfiles/vertical.png')
		avg = bv.avg_row(frame)
		expected = [[0,0,0],[255,255,255],[0,0,0]]
		np.testing.assert_array_equal(avg,expected)

	def test_avg_column(self):
		frame = cv2.imread('testfiles/horizontal.png')
		avg = bv.avg_column(frame)
		expected = [[255,255,255],[0,0,0],[255,255,255]]
		np.testing.assert_array_equal(avg,expected)

	def test_avg_pixel(self):
		frame = cv2.imread('testfiles/horizontal.png')
		avg = bv.avg_pixel(frame)
		single = np.floor(6*255/9.0)
		expected = [single,single,single]
		np.testing.assert_array_equal(avg,expected)

class TestBarcodeMakers(unittest.TestCase):

	def test_barcode_horizontal(self):
		expected_path = 'testfiles/horizontal_expected.png'
		output_path = 'testfiles/horizontal_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_horizontal(vid_path='testfiles/horizontal.mov',mod_frames=10,pixels_per_frame=1,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_vertical(self):
		expected_path = 'testfiles/vertical_expected.png'
		output_path = 'testfiles/vertical_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_vertical(vid_path='testfiles/vertical.mov',mod_frames=10,pixels_per_frame=1,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_vertical_on_hz(self):
		expected_path = 'testfiles/vertical_onHorizontal_expected.png'
		output_path = 'testfiles/vertical_onHorizontal_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_vertical(vid_path='testfiles/horizontal.mov',mod_frames=10,pixels_per_frame=1,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode(self):
		expected_path = 'testfiles/barcode_expected.png'
		output_path = 'testfiles/barcode_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode(vid_path='testfiles/horizontal.mov',mod_frames=10,bar_height=20,pixels_per_frame=1,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_circle_bgBlack(self):
		expected_path = 'testfiles/barcode_circle_black_expected.png'
		output_path = 'testfiles/barcode_circle_black_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_circle(vid_path='testfiles/horizontal.mov',mod_frames=10,background=0,dim=100,thickness=10,radius=30,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_circle_bgWhite(self):
		expected_path = 'testfiles/barcode_circle_white_expected.png'
		output_path = 'testfiles/barcode_circle_white_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_circle(vid_path='testfiles/horizontal.mov',mod_frames=10,background=255,dim=100,thickness=10,radius=30,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_spiral_bgBlack(self):
		expected_path = 'testfiles/barcode_spiral_black_expected.png'
		output_path = 'testfiles/barcode_spiral_black_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_spiral(vid_path='testfiles/horizontal.mov',mod_frames=10,background=0,dim=100,thickness=10,radius=30,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

	def test_barcode_circle_bgWhite(self):
		expected_path = 'testfiles/barcode_spiral_white_expected.png'
		output_path = 'testfiles/barcode_spiral_white_out.png'
		if os.path.isfile(output_path):
			os.remove(output_path)
		else:
			pass
		bv.barcode_spiral(vid_path='testfiles/horizontal.mov',mod_frames=10,background=255,dim=100,thickness=10,radius=30,filename_output=output_path)
		expected = cv2.imread(expected_path)
		made = cv2.imread(output_path)
		np.testing.assert_array_equal(made,expected)

if __name__ == '__main__':
	unittest.main()