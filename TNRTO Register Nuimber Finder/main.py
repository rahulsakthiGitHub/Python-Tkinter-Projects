from tkinter import*
import tkinter as tk

win=tk.Tk()
win.title("TNRTO Register Number Finder")
win.configure(bg="Green")

global e,key

def erase(self):
    e.delete(0,END)

def result():
    key=tk.StringVar()
    key=e.get()
    
    if(key=="TN01"):
        L2=Label(win,text="Chennai Central ( சென்னை சென்ட்ரல் )")
        L2.pack()
    if(key=="TN13"):
        L2=Label(win,text="Ambattur ( அம்பத்தூர் )")
        L2.pack()
    if(key=="TN97"):
        L2=Label(win,text="Arani ( ஆரணி )")
        L2.pack()
    if(key=="TN61"):
        L2=Label(win,text="Ariyalur ( அரியலூர் )")
        L2.pack()
    if(key=="TN77"):
        L2=Label(win,text="Attur ( ஆத்தூர் )")
        L2.pack()
    if(key=="TN19"):
        L2=Label(win,text="Chengalpattu ( செங்கல்பட்டு )")
        L2.pack()
    if(key=="TN04"):
        L2=Label(win,text="Chennai East ( சென்னை கிழக்கு )")
        L2.pack()
    if(key=="TN05"):
        L2=Label(win,text="Chennai North ( சென்னை வடக்கு )")
        L2.pack()
    if(key=="TN03"):
        L2=Label(win,text="Chennai North East ( சென்னை வடகிழக்கு )")
        L2.pack()
    if(key=="TN02"):
        L2=Label(win,text="Chennai North West ( சென்னை வடமேற்கு )")
        L2.pack()
    if(key=="TN07"):
        L2=Label(win,text="Chennai South ( சென்னை தெற்கு )")
        L2.pack()
    if(key=="TN06"):
        L2=Label(win,text="Chennai South East ( சென்னை தென்கிழக்கு )")
        L2.pack()
    if(key=="TN10"):
        L2=Label(win,text="Chennai South West ( சென்னை தென்மேற்கு )")
        L2.pack()
    if(key=="TN09"):
        L2=Label(win,text="Chennai West ( சென்னை மேற்கு ) ")
        L2.pack()
    if(key=="TN91"):
        L2=Label(win,text="Chidambaram ( சிதம்பரம் )")
        L2.pack()
    if(key=="TN66"):
        L2=Label(win,text="Coimbatore Central ( கோயம்புத்தூர் சென்ட்ரல் )")
        L2.pack()
    if(key=="TN38"):
        L2=Label(win,text="Coimbatore North ( கோவை வடக்கு )")
        L2.pack()
    if(key=="TN37"):
        L2=Label(win,text="Coimbatore South ( கோவை தெற்கு )")
        L2.pack()
    if(key=="TN99"):
        L2=Label(win,text="Coimbatore West ( கோவை மேற்கு )")
        L2.pack()
    if(key=="TN31"):
        L2=Label(win,text="Cuddalore ( கடலூர் )")
        L2.pack()
    if(key=="TN78"):
        L2=Label(win,text="Dharapuram ( தாராபுரம் )")
        L2.pack()
    if(key=="TN29"):
        L2=Label(win,text="Dharmapuri ( தருமபுரி )")
        L2.pack()
    if(key=="TN57"):
        L2=Label(win,text="Dindigul ( திண்டுக்கல் )")
        L2.pack()
    if(key=="TN33"):
        L2=Label(win,text="Erode East ( ஈரோடு கிழக்கு )")
        L2.pack()
    if(key=="TN86"):
        L2=Label(win,text="Erode West ( ஈரோடு மேற்கு )")
        L2.pack()
    if(key=="TN36"):
        L2=Label(win,text="Gobichettipalayam ( கோபிசெட்டிபாளையம் )")
        L2.pack()
    if(key=="TN70"):
        L2=Label(win,text="Hosur ( ஓசூர் )")
        L2.pack()
    if(key=="TN21"):
        L2=Label(win,text="Kanchipuram ( காஞ்சிபுரம் )")
        L2.pack()
    if(key=="TN47"):
        L2=Label(win,text="Karur ( கரூர் )")
        L2.pack()
    if(key=="TN96"):
        L2=Label(win,text="Kovilpatti ( கோவில்பட்டி )")
        L2.pack()
    if(key=="TN24"):
        L2=Label(win,text="Krishnagiri ( கிருஷ்ணகிரி )")
        L2.pack()
    if(key=="TN68"):
        L2=Label(win,text="Kumbakonam ( கும்பகோணம் )")
        L2.pack()
    if(key=="TN85"):
        L2=Label(win,text="Kundrathur ( குன்றத்தூர் )")
        L2.pack()
    if(key=="TN64"):
        L2=Label(win,text="Madurai Central ( மதுரை மத்திய )")
        L2.pack()
    if(key=="TN59"):
        L2=Label(win,text="Madurai North ( மதுரை வடக்கு )")
        L2.pack()
    if(key=="TN58"):
        L2=Label(win,text="Madurai South ( மதுரை தெற்கு )")
        L2.pack()
    if(key=="TN75"):
        L2=Label(win,text="Marthandam ( மார்த்தாண்டம் )")
        L2.pack()
    if(key=="TN82"):
        L2=Label(win,text="Mayiladuthurai ( மயிலாடுதுறை )")
        L2.pack()
    if(key=="TN22"):
        L2=Label(win,text="Meenambakkam ( மீனம்பாக்கம் )")
        L2.pack()
    if(key=="TN40"):
        L2=Label(win,text="Mettupalayam ( மேட்டுப்பாளையம் )")
        L2.pack()
    if(key=="TN93"):
        L2=Label(win,text="Mettur ( மேட்டூர் )")
        L2.pack()
    if(key=="TN51"):
        L2=Label(win,text="Nagapattinam ( நாகப்பட்டினம் )")
        L2.pack()
    if(key=="TN74"):
        L2=Label(win,text="Nagercoil ( நாகர்கோவில் )")
        L2.pack()
    if(key=="TN28"):
        L2=Label(win,text="Namakkal North ( நாமக்கல் வடக்கு )")
        L2.pack()
    if(key=="TN88"):
        L2=Label(win,text="Namakkal South ( நாமக்கல் தெற்கு )")
        L2.pack()
    if(key=="TN43"):
        L2=Label(win,text="Ooty ( ஊட்டி )")
        L2.pack()
    if(key=="TN94"):
        L2=Label(win,text="Palani ( பழனி )")
        L2.pack()
    if(key=="TN46"):
        L2=Label(win,text="Perambalur ( பெரம்பலூர் )")
        L2.pack()
    if(key=="TN56"):
        L2=Label(win,text="Perundurai ( பெருந்துறை )")
        L2.pack()
    if(key=="TN41"):
        L2=Label(win,text="Pollachi ( பொள்ளாச்சி )")
        L2.pack()
    if(key=="TN12"):
        L2=Label(win,text="Poonamallee ( பூந்தமல்லி )")
        L2.pack()
    if(key=="TN55"):
        L2=Label(win,text="Pudukottai ( புதுக்கோட்டை )")
        L2.pack()
    if(key=="TN65"):
        L2=Label(win,text="Ramanathapuram ( ராமநாதபுரம் )")
        L2.pack()
    if(key=="TN73"):
        L2=Label(win,text="Ranipet ( ராணிப்பேட்டை )")
        L2.pack()
    if(key=="TN18"):
        L2=Label(win,text="Redhills ( ரெட்ஹில்ஸ் )")
        L2.pack()
    if(key=="TN27"):
        L2=Label(win,text="Salem ( சேலம் )")
        L2.pack()
    if(key=="TN54"):
        L2=Label(win,text="Salem East ( சேலம் கிழக்கு )")
        L2.pack()
    if(key=="TN90"):
        L2=Label(win,text="Salem West ( சேலம் மேற்கு )")
        L2.pack()
    if(key=="TN79"):
        L2=Label(win,text="Sankarankovil ( சங்கரன்கோவில் )")
        L2.pack()
    if(key=="TN52"):
        L2=Label(win,text="Sivakigi ( சங்கரி )")
        L2.pack()
    if(key=="TN14"):
        L2=Label(win,text="Sholinganallur ( சோழிங்கநல்லூர் )")
        L2.pack()
    if(key=="TN63"):
        L2=Label(win,text="Sivaganga ( சிவகங்கை )")
        L2.pack()
    if(key=="TN95"):
        L2=Label(win,text="Sivakasi ( சிவகாசி )")
        L2.pack()
    if(key=="TN87"):
        L2=Label(win,text="Sriperumbundur ( ஸ்ரீபெரும்புதூர் )")
        L2.pack()
    if(key=="TN48"):
        L2=Label(win,text="Srirangam ( ஸ்ரீரங்கம் )")
        L2.pack()
    if(key=="TN84"):
        L2=Label(win,text="Srivilliputtur ( ஸ்ரீவில்லிபுத்தூர் )")
        L2.pack()
    if(key=="TN11"):
        L2=Label(win,text="Tambaram ( தாம்பரம் )")
        L2.pack()
    if(key=="TN76"):
        L2=Label(win,text="Tenkasi ( தென்காசி )")
        L2.pack()
    if(key=="TN49"):
        L2=Label(win,text="Thanjavur ( தஞ்சாவூர் )")
        L2.pack()
    if(key=="TN60"):
        L2=Label(win,text="Theni ( தேனி )")
        L2.pack()
    if(key=="TN92"):
        L2=Label(win,text="Thiruchendur ( திருச்செந்தூர் )")
        L2.pack()
    if(key=="TN50"):
        L2=Label(win,text="Thiruvarur ( திருவாரூர் )")
        L2.pack()
    if(key=="TN81"):
        L2=Label(win,text="Thiruverumbur East ( திருவெறும்பூர் கிழக்கு )")
        L2.pack()
    if(key=="TN16"):
        L2=Label(win,text="Tindivanam ( திண்டிவனம் )")
        L2.pack()
    if(key=="TN34"):
        L2=Label(win,text="Tiruchengode ( திருச்செங்கோடு )")
        L2.pack()
    if(key=="TN45"):
        L2=Label(win,text="Tiruchirappalli West ( திருச்சிராப்பள்ளி மேற்கு )")
        L2.pack()
    if(key=="TN72"):
        L2=Label(win,text="Tirunelveli ( திருநெல்வேலி )")
        L2.pack()
    if(key=="TN39"):
        L2=Label(win,text="Tiruppur North ( திருப்பூர் வடக்கு )")
        L2.pack()
    if(key=="TN42"):
        L2=Label(win,text="Tiruppur South  ( திருப்பூர் தெற்கு )")
        L2.pack()
    if(key=="TN20"):
        L2=Label(win,text="Tiruvallur ( திருவள்ளூர் )")
        L2.pack()
    if(key=="TN25"):
        L2=Label(win,text="Tiruvannamalai ( திருவண்ணாமலை )")
        L2.pack()
    if(key=="TN69"):
        L2=Label(win,text="Tuticorin ( தூத்துக்குடி )")
        L2.pack()
    if(key=="TN15"):
        L2=Label(win,text="Ulundurpet ( உளுந்தூர்பேட்டை )")
        L2.pack()
    if(key=="TN83"):
        L2=Label(win,text="Vaniyambadi ( வாணியம்பாடி )")
        L2.pack()
    if(key=="TN23"):
        L2=Label(win,text="Vellore ( வேலூர் )")
        L2.pack()
    if(key=="TN32"):
        L2=Label(win,text="Villupuram ( விழுப்புரம் )")
        L2.pack()
    if(key=="TN67"):
        L2=Label(win,text="Virudhunager ( விருதுநகர் )")
        L2.pack()

    if(key==""):
        L2=Label(win,text="Invalid Data",fg="White",bg="red")
        L2.pack()
        

L=Label(win,text="TNRTO Register Number Finder",font=("Times New Roman",20,"bold"))
L.pack(pady=20)

e=Entry(win,width=20,borderwidth=3)
e.pack(pady=30)
e.insert(0,"Enter Number here")
e.bind('<Button-1>',erase)


btn=Button(win,text="Submit",font=(20),activeforeground="green",activebackground="Yellow",command=result)
btn.pack(pady=10)

note=Label(win,text="Note: Please Enter following format TN01 ",bg='green',fg='yellow',font=('bold'))
note.pack()

win.mainloop()
