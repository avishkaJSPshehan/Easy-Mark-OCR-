from tkinter import *
from PIL import ImageTk, Image
import webbrowser

root=Tk()
root.title('Easy Marker')
root.geometry("550x300+100+50")

url = ''
path = "c7.jpeg"

all_ans = []

############################################################################

def about_us():
	webbrowser.open_new("https://sites.google.com/view/about-us404/home")

def getAns():

	all_ans.append(A1.get())
	all_ans.append(A2.get())
	all_ans.append(A3.get())
	all_ans.append(A4.get())
	all_ans.append(A5.get())
	all_ans.append(A6.get())
	all_ans.append(A7.get())
	all_ans.append(A8.get())
	all_ans.append(A9.get())
	all_ans.append(A10.get())

	all_ans.append(A11.get())
	all_ans.append(A12.get())
	all_ans.append(A13.get())
	all_ans.append(A14.get())
	all_ans.append(A15.get())
	all_ans.append(A16.get())
	all_ans.append(A17.get())
	all_ans.append(A18.get())
	all_ans.append(A19.get())
	all_ans.append(A20.get())

	all_ans.append(A21.get())
	all_ans.append(A22.get())
	all_ans.append(A23.get())
	all_ans.append(A24.get())
	all_ans.append(A25.get())
	all_ans.append(A26.get())
	all_ans.append(A27.get())
	all_ans.append(A28.get())
	all_ans.append(A29.get())
	all_ans.append(A30.get())

	all_ans.append(A31.get())
	all_ans.append(A32.get())
	all_ans.append(A33.get())
	all_ans.append(A34.get())
	all_ans.append(A35.get())
	all_ans.append(A36.get())
	all_ans.append(A37.get())
	all_ans.append(A38.get())
	all_ans.append(A39.get())
	all_ans.append(A40.get())

	all_ans.append(A41.get())
	all_ans.append(A42.get())
	all_ans.append(A43.get())
	all_ans.append(A44.get())
	all_ans.append(A45.get())
	all_ans.append(A46.get())
	all_ans.append(A47.get())
	all_ans.append(A48.get())
	all_ans.append(A49.get())
	all_ans.append(A50.get())


	print(all_ans)

def set_new_paper():

	global A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38,A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50

	set_paper_win = Toplevel(root)
	set_paper_win.title("Set New Paper")
	set_paper_win.geometry("600x300+675+50")
	set_paper_win.configure(bg='white')

	# A Label widget to show in toplevel
	Label(set_paper_win, text="Q u e s t I o n s   C o u n t  ", fg='black',bg='white', font=("Britannic Bold", 10)).place(x=10, y=10)
	Label(set_paper_win, text="Q u e s t I o n s   F e l d  ", fg='black',bg='white', font=("Britannic Bold", 10)).place(x=10, y=40)
	Label(set_paper_win, text="Q u e s t I o n s   I n   F e l d  ", fg='black',bg='white', font=("Britannic Bold", 10)).place(x=10, y=70)
	Label(set_paper_win, text="M a r k  C o r r e c t  A n s w e r s  ", fg='black',bg='white', font=("Britannic Bold", 10)).place(x=200, y=100)


	Q_count = Entry(set_paper_win,width=9,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	Q_count.place(x=215,y=10)
	Frame(set_paper_win,width=80,height=2,bg="black").place(x=215,y=28)

	Q_feld = Entry(set_paper_win,width=9,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	Q_feld.place(x=215,y=40)
	Frame(set_paper_win,width=80,height=2,bg="black").place(x=215,y=58)

	Q_in_feld = Entry(set_paper_win,width=9,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	Q_in_feld.place(x=215,y=70)
	Frame(set_paper_win,width=80,height=2,bg="black").place(x=215,y=88)

	frame1 = Frame(set_paper_win,highlightbackground="blue", highlightthickness=2,bg='white')
	frame1.place(x = 10,y = 120)

	Label(frame1, text = "01 :\t06 :\t11 :\t16 :\t21 :\t26 :\t31 :\t36 :\t41 :\t46 :\t", width=92, anchor="w",bg = 'white',font=("Britannic Bold", 8)).pack(padx=10, pady=5)
	Label(frame1, text = "02 :\t07 :\t12 :\t17 :\t22 :\t27 :\t32 :\t37 :\t42 :\t47 :\t", width=92, anchor="w",bg = 'white',font=("Britannic Bold", 8)).pack(padx=10, pady=5)
	Label(frame1, text = "03 :\t08 :\t13 :\t18 :\t23 :\t28 :\t33 :\t38 :\t43 :\t48 :\t", width=92, anchor="w",bg = 'white',font=("Britannic Bold", 8)).pack(padx=10, pady=5)
	Label(frame1, text = "04 :\t09 :\t14 :\t19 :\t24 :\t29 :\t34 :\t39 :\t44 :\t49 :\t", width=92, anchor="w",bg = 'white',font=("Britannic Bold", 8)).pack(padx=10, pady=5)
	Label(frame1, text = "05 :\t10 :\t15 :\t20 :\t25 :\t30 :\t35 :\t40 :\t45 :\t50 :\t", width=92, anchor="w",bg = 'white',font=("Britannic Bold", 8)).pack(padx=10, pady=5)

	A1 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A1.place(x=48,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=48,y=142)

	A2 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A2.place(x=48,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=48,y=170)

	A3 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A3.place(x=48,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=48,y=198)

	A4 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A4.place(x=48,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=48,y=226)

	A5 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A5.place(x=48,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=48,y=254)



	A6 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A6.place(x=103,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=103,y=142)

	A7 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A7.place(x=103,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=103,y=170)

	A8 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A8.place(x=103,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=103,y=198)

	A9 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A9.place(x=103,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=103,y=226)

	A10 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A10.place(x=103,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=103,y=254)



	A11 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A11.place(x=160,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=160,y=142)

	A12 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A12.place(x=160,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=160,y=170)

	A13 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A13.place(x=160,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=160,y=198)

	A14 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A14.place(x=160,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=160,y=226)

	A15 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A15.place(x=160,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=160,y=254)



	A16 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A16.place(x=215,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=215,y=142)

	A17 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A17.place(x=215,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=215,y=170)

	A18 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A18.place(x=215,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=215,y=198)

	A19 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A19.place(x=215,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=215,y=226)

	A20 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A20.place(x=215,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=213,y=254)


	A21 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A21.place(x=270,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=270,y=142)

	A22 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A22.place(x=270,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=270,y=170)

	A23 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A23.place(x=270,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=270,y=198)

	A24 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A24.place(x=270,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=270,y=226)

	A25 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A25.place(x=270,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=270,y=254)



	A26 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A26.place(x=325,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=325,y=142)

	A27 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A27.place(x=325,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=325,y=170)

	A28 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A28.place(x=325,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=325,y=198)

	A29 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A29.place(x=325,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=325,y=226)

	A30 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A30.place(x=325,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=325,y=254)



	A31 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A31.place(x=380,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=380,y=142)

	A32 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A31.place(x=380,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=380,y=170)

	A33 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A33.place(x=380,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=380,y=198)

	A34 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A34.place(x=380,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=380,y=226)

	A35 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A35.place(x=380,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=380,y=254)



	A36 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A36.place(x=435,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=435,y=142)

	A37 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A37.place(x=435,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=435,y=170)

	A38 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A38.place(x=435,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=435,y=198)

	A39 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A39.place(x=435,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=435,y=226)

	A40 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A40.place(x=435,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=435,y=254)




	A41 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A41.place(x=490,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=490,y=142)

	A42 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A42.place(x=490,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=490,y=170)

	A43 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A43.place(x=490,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=490,y=198)

	A44 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A44.place(x=490,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=490,y=226)

	A45 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A45.place(x=490,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=490,y=254)




	A46 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A46.place(x=545,y=126)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=545,y=142)

	A47 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A47.place(x=545,y=154)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=545,y=170)

	A48 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A48.place(x=545,y=182)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=545,y=198)

	A49 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A49.place(x=545,y=210)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=545,y=226)

	A50 = Entry(set_paper_win,width=3,fg="black",bg="white",border=0,font=("Britannic Bold", 10,"bold"))
	A50.place(x=545,y=238)
	Frame(set_paper_win,width=30,height=2,bg="black").place(x=545,y=254)
	


	save_btn=Button(set_paper_win, text="S a v e", fg='black',bg = "#4287f5",font=("Britannic Bold", 10), padx = 270,border =  0,command=getAns)
	save_btn.place(x=10, y=270)

def mark_paper():
	import cv2
	import numpy as np
	import utlis
	import urllib.request
	import numpy as np
	import imutils

	#############################################################
	
	widthImg = 700
	heightImg = 700
	questions =  10
	choices = 5
	ans = []
	i = 0
	while True:
		if(all_ans[i] != ''):
			ans.append((int(all_ans[i]))-1)
			i += 1
		else:
			break
	
	webcamFeed = True
	cameraNo = 1

	url = ip_address.get()
	url += '/shot.jpg'
	print(url)
	#############################################################

	cap = cv2.VideoCapture(cameraNo)
	cap.set(10,150)




	while(True):

		if(url == '/shot.jpg'):
			img = cv2.imread(path)
		else:
			imgPath = urllib.request.urlopen(url)
			imgNp = np.array(bytearray(imgPath.read()),dtype=np.uint8)
			img = cv2.imdecode(imgNp,-1)
			img = imutils.resize(img,width=450)
		#cv2.imshow("CameraFeed",img)

			
												
		if(ord('q')==cv2.waitKey(1)):
			exit(0)

		'''if(webcamFeed): 
			success,img = cap.read()
		else:
			img = cv2.imread(path)'''

		img = cv2.resize(img,(widthImg,heightImg))
		imgContours  = img.copy()
		imgFinal  = img.copy()
		imgBiggestContours  = img.copy()
		imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
		imgCanny = cv2.Canny(imgBlur,10,50)

		try:

			countours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
			cv2.drawContours(imgContours,countours,-1,(255,0,0),5)

			rectCon = utlis.rectCountours(countours)
			biggestContour = utlis.getCornerPoints(rectCon[0])
			gradePoints = utlis.getCornerPoints(rectCon[1])


			#print(biggestContour)

			if(biggestContour.size !=  0 and gradePoints.size !=  0):

				cv2.drawContours(imgBiggestContours,biggestContour,-1,(0,255,0),20)
				cv2.drawContours(imgBiggestContours,gradePoints,-1,(0,0,255),20)

				biggestContour = utlis.reorder(biggestContour)
				gradePoints = utlis.reorder(gradePoints)

				pt1 = np.float32(biggestContour)
				pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
				matrix = cv2.getPerspectiveTransform(pt1,pt2)
				imgWarpColored = cv2.warpPerspective(img,matrix,(widthImg,heightImg))

				ptG1 = np.float32(gradePoints)
				ptG2 = np.float32([[0,0],[325,0],[0,150],[325,150]])
				matrixG = cv2.getPerspectiveTransform(ptG1,ptG2)
				imgGradeDisplay = cv2.warpPerspective(img,matrixG,(widthImg,heightImg))
				#cv2.imshow("Grade ",imgGradeDisplay)

				imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
				imgThresh = cv2.threshold(imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]

				boxes = utlis.splitBoxes(imgThresh)
				#cv2.imshow("Test ",boxes[1])
				#print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[2]))




				myPixelVal = np.zeros((questions,choices))
				countC = 0
				countR = 0

				for image in boxes:
					totalPixels = cv2.countNonZero(image)
					myPixelVal[countR][countC] = totalPixels
					countC += 1
					if(countC == choices):countR += 1  ; countC = 0
				#print(myPixelVal)


				myIndex = []
				for x in range(0,questions):
					arr = myPixelVal[x]
					#print("arr ",arr)
					myIndexVal = np.where(arr==np.amax(arr))
					#print(myIndexVal[0])
					myIndex.append(myIndexVal[0][0])
				print(myIndex)

				grading =[]
				for x in range(0,questions):
					if(ans[x] == myIndex[x]):
						grading.append(1)
					else:
						grading.append(0)

				print(grading)
				score = (sum(grading)/questions)*100
				print(score) 

				imgResult = imgWarpColored.copy()
				imgResult = utlis.showAnswers(imgResult,myIndex,grading,ans,questions,choices)
				imgRawDrawing = np.zeros_like(imgWarpColored)
				imgRawDrawing = utlis.showAnswers(imgRawDrawing,myIndex,grading,ans,questions,choices)
				invmatrix = cv2.getPerspectiveTransform(pt2,pt1)
				imgInvWarp = cv2.warpPerspective(imgRawDrawing,invmatrix,(widthImg,heightImg))

				imgRawGrade = np.zeros_like(imgGradeDisplay)
				cv2.putText(imgRawGrade,str(int(score))+"%",(60,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,255),3)
				invMatrixG = cv2.getPerspectiveTransform(ptG2,ptG1)
				imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade,invMatrixG,(widthImg,heightImg))


				imgFinal = cv2.addWeighted(imgFinal,1,imgInvWarp,1,0)
				imgFinal = cv2.addWeighted(imgFinal,1,imgInvGradeDisplay,1,0)




			imgBlank = np.zeros_like(img)
			imageArray = ([img,imgGray,imgBlur,imgCanny], 
							[imgContours,imgBiggestContours,imgWarpColored,imgThresh],
							[imgResult,imgRawDrawing,imgInvWarp,imgFinal])


		except:
			imgBlank = np.zeros_like(img)
			imageArray = ([img,imgGray,imgBlur,imgCanny], 
							[imgBlank,imgBlank,imgBlank,imgBlank],
							[imgBlank,imgBlank,imgBlank,imgBlank])

		imgStacked = utlis.stackImages(imageArray,0.3)

		cv2.imshow("Final Result",imgFinal)
		cv2.imshow("Stacked Image",imgStacked)
		if(cv2.waitKey(1) & 0xFF == ord('s')):
			cv2.inwrite("Final Result.jpg",imgFinal)
			cv2.waitKey(300)


############################################################################

img_frame = Frame(root, width=550, height=300)
img_frame.configure(bg='white')
img_frame.place(x=0,y=0)
img_frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("background_3_275x300.jpg"))

# Create a Label Widget to display the text or Image
label = Label(img_frame, image = img,border = 0)
label.place(x = 0,y = 0)


Label(root, text="E a s yM a r k", fg='black',bg='white', font=("Bauhaus 93", 25)).place(x=290, y=40)
set_new_paper_btn=Button(root, text="Set New Paper", fg='black',bg = "#4287f5",font=("Bauhaus 93", 15), padx = 30,border =  0,command = set_new_paper)
set_new_paper_btn.place(x=285, y=90)


Label(root, text="S e r v e r   I P   A d d r e s s", fg='black',bg='white', font=("Arial Black", 10),).place(x=285, y=130)
ip_address = Entry(root,width=28,fg="black",bg="white",border=0,font=("times new roman", 10,"bold"))
ip_address.place(x=285,y=160)
Frame(root,width=197,height=2,bg="black").place(x=285,y=178)

mark_paper_btn=Button(root, text="Mark Paper", fg='black',bg = "#4287f5",font=("Bauhaus 93", 15), padx = 42,border =  0,command = mark_paper)
mark_paper_btn.place(x=285, y=185)

about_us_btn=Button(root, text="   About Us  ", fg='black',bg = "#DC143C",font=("Bauhaus 93", 15), padx = 42,border =  0,command = about_us)
about_us_btn.place(x=285, y=225)

Label(root, text="P   O   W   E   R   E   D          B   Y          4   0   4", fg='black',bg='white', font=("Bauhaus 93", 10)).place(x=140, y=280)


root.mainloop()