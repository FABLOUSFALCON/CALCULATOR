from tkinter  import ttk , Button , Tk , Frame, Text , FALSE , DISABLED , CHAR, FLAT, NORMAL, END
import tkinter



num1 = 0

num2 = 0

sign = "x"

tryy = 1

px = 1

py = 1

pp = 1

pill = int
root = Tk()

# root.wm_iconbitmap("icon.ico")
root.title("Calculator")
root.geometry("321x492+600+200")
root.resizable(FALSE , FALSE)
f1  = Frame(root,width = 350 , height = 170,bg = "orange")
f1.pack()

f2 = Frame(root,width = 350 , height = 330)
f2.pack()

 
tb = Text(f1, fg = "BLACK" ,bg = "orange",font = ("Times",35) ,state = DISABLED , pady = 30 , padx = 10,width = 13)
tb.config(wrap = CHAR,relief = FLAT)
tb.place(x=0,y=0)

f3  = Frame( f1 ,width = 350 , height = 20,bg = "red")
f3.place( x = 0 , y = 5)

tb1 = Text(f3, fg = "BLACK" ,bg = "orange",font = ("Times",12) ,state = DISABLED , pady = 0 , padx = 10,width = 50)
tb1.config(wrap = CHAR,relief = FLAT)
tb1.place(x=0,y=0)


def lock():
  butr.config(state = DISABLED)
  bute.config(state = DISABLED)
  butmi.config(state = DISABLED)
  butp.config(state = DISABLED)
  butm.config(state = DISABLED)
  butdi.config(state = DISABLED)
  butd.config(state = DISABLED)
  butplus.config(state = DISABLED)
  bc1.config(state = DISABLED)
  bc2.config(state = DISABLED)
  bc3.config(state = DISABLED)
  bc4.config(state = DISABLED)

def unlock():
  butr.config(state = NORMAL)
  bute.config(state = NORMAL)
  butmi.config(state = NORMAL)
  butp.config(state = NORMAL)
  butm.config(state = NORMAL)
  butdi.config(state = NORMAL)
  butd.config(state = NORMAL)
  butplus.config(state = NORMAL)
  bc1.config(state = NORMAL)
  bc2.config(state = NORMAL)
  bc3.config(state = NORMAL)
  bc4.config(state = NORMAL)

def tx():
  global px
  global py

  v = str(num1)
  v1 = v.split(".")
 

  if len(v1) == 2:
   if v1[1] == '0' :
    v = v1[0]
  else:
    v = v1[0]  
  if py == 1 :
   tb1.config(state = NORMAL)
   tb1.insert(END, (f"{v} {sign1} ") )
   tb1.config(state = DISABLED)
   py = py + 1
  else: 
   clearx()
   px = 1
   tb1.config(state = NORMAL)
   tb1.insert(END, (f"{v} {sign1} ") )
   tb1.config(state = DISABLED)
     

def ty():
  gx = tb1.get(1.0 , END)
  gx = str(gx) 
  g1x = list(gx)
  
  
  clearx()
  v = str(con)
  v1 = v.split(".")
  if len(v1) == 2:
   if v1[1] == '0' :
    v = v1[0]
  else:
    v = v1[0]    
 
    
  tb1.config(state = NORMAL)
  tb1.insert(END, (f"{v} {sign1} ") )
  tb1.config(state = DISABLED)
   
  vx = str(num2)
  v1x = vx.split(".")
  if len(v1x) == 2:
   if v1x[1] == '0' :
     vx = v1[0]
  else:
     vx = v1[0]    
  
   
  if '=' not in g1x:
   tb1.config(state = NORMAL)
   tb1.insert(END, (f"{vx} {sign2} ") )
   tb1.config(state = DISABLED)
  else:
   tb1.config(state = NORMAL)
   tb1.insert(END, (f"{vx} {sign2} ") )
   tb1.config(state = DISABLED)  
  
  
def scr():
 tb.config(state = NORMAL)
 tb.insert(END , 0)
 tb.config(state = DISABLED)
scr()
def clear():
    unlock()
    tb.config(font = ("Times",35)) 
    tb.config(state = NORMAL)
    tb.delete(1.0 , END)
    tb.config(state = DISABLED)
    
def clearx():
  tb1.config(state = NORMAL)
  tb1.delete(1.0 , END)
  tb1.config(state = DISABLED)    
def clearb(*args):
    global num1
    global px
    global pp
    unlock()
    tb.config(state = NORMAL)
    tb.delete(1.0 , END)
    tb.insert(1.0 , 0)
    tb.config(state = DISABLED)
    
    tb1.config(state = NORMAL)
    tb1.delete(1.0 , END)
    tb1.config(state = DISABLED) 
    num1 = 0  
    px = 1  
    pp = 1
def clear1b(*args):
    global num1
    global pp
    
    unlock()
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if sign != 'x':
     bx2 = tb.get(1.0 , END)
     bx2 = str(bx2)
     bx2x = list(bx2)
     bx2x.pop(-1)
     bbs = "".join(bx2x)
     bnum = float(bbs)
     
     
    by = tb1.get(1.0 , END)
    b1y = str(by)
    bxy = list(b1y)
    
    if bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O':
     clear()   
    tb.config(state = NORMAL)
    num1z = tb.get(1.0 , END)
    list1z = list(num1z)
    x = len(list1z)
  
    if ('+' in bxy or 'x' in bxy or '/' in bxy or '-' in bxy) and (num1 == bnum)  :
      clearb()
    elif x == 2:
        clearb()
    else:    
     x = x - 2
     tb.delete(f"1.{x}" , END)
     tb.config(state = DISABLED)
    
      
     
def clear1():
    unlock()
    
    tb.config(state = NORMAL)
    num1 = tb.get(1.0 , END)
    list1 = list(num1)
    x = len(list1)
    x = x - 2
    tb.delete(f"1.{x}" , END)
    tb.config(state = DISABLED)
    
    # tb1.config(state = NORMAL)
    # numx = tb1.get(1.0 , END)
    # listx = list(numx)
    # y = len(listx)
    # y = y - 2
    # tb1.delete(f"1.{x}" , END)
    # tb1.config(state = DISABLED)    
        


def type0(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,0)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,0)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,0)
     tb.config(state = DISABLED)

    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,0)
     tb.insert(END,0)
     tb.config(state = DISABLED)
     tryy = tryy +1            
         
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,0)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,0)
     tb.config(state = DISABLED)    
        
def type1(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,1)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,1)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,1)
     tb.config(state = DISABLED)
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,1)
     tb.insert(END,1)
     tb.config(state = DISABLED)
     tryy = tryy +1            
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,1)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
     tb.config(state = NORMAL)
     tb.insert(END,1)
     tb.config(state = DISABLED)   
      
def type2(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,2)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,2)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,2)
     tb.config(state = DISABLED) 
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,2)
     tb.insert(END,2)
     tb.config(state = DISABLED)
     tryy = tryy +1           
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,2)
     tb.config(state = DISABLED)
     tryy = tryy + 1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,2)
     tb.config(state = DISABLED)    
    
def type3(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,3)
     tb.config(state = DISABLED)
     pp = 1 
    
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,3)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,3)
     tb.config(state = DISABLED)
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,3)
     tb.insert(END,3)
     tb.config(state = DISABLED)
     tryy = tryy +1                 
    elif sign != 'x' and tryy == 1:
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,3)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,3)
     tb.config(state = DISABLED)  
       
def type4(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,4)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,4)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,4)
     tb.config(state = DISABLED)
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,4)
     tb.insert(END,4)
     tb.config(state = DISABLED)
     tryy = tryy +1                 
    elif sign != 'x' and tryy == 1:
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,4)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,4)
     tb.config(state = DISABLED)    
    
def type5(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    

    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,5)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,5)
     tb.config(state = DISABLED)
     
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,5)
     tb.config(state = DISABLED)
  
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()   
     clearx() 
     tb.config(state = NORMAL)
     tb.insert(END,5)
     tb.insert(END,5)
     tb.config(state = DISABLED)
     tryy = tryy +1  
     
         
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,5)
     tb.config(state = DISABLED)
     tryy = tryy +1
     
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,5)
     tb.config(state = DISABLED)
    
def type6(*args):
    global tryy
    global pp
    
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,6)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,6)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,6)
     tb.config(state = DISABLED)   
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,6)
     tb.insert(END,6)
     tb.config(state = DISABLED)
     tryy = tryy +1              
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,6)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,6)
     tb.config(state = DISABLED)    
    
def type7(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,7)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,7)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,7)
     tb.config(state = DISABLED)  
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,7)
     tb.insert(END,7)
     tb.config(state = DISABLED)
     tryy = tryy +1               
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,7)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,7)
     tb.config(state = DISABLED)    
     
def type8(*args):
    global tryy
    global pp
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,8)
     tb.config(state = DISABLED)
     pp = 1 
     
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     tb.config(state = NORMAL)
     tb.insert(END,8)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,8)
     tb.config(state = DISABLED)  
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,8)
     tb.insert(END,8)
     tb.config(state = DISABLED)
     tryy = tryy +1               
    elif sign != 'x' and tryy == 1 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,8)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,8)
     tb.config(state = DISABLED) 
        
def type9(*args):
    global tryy
    global pp
    
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    
    if len(bx) >= 27 and (pp == 1 or pp == 0) :
     pass
    elif len(bx) >= 27 and pp != 1:
     tb.config(state = NORMAL)
     tb.delete(1.0 , END)
     tb.insert(END,9)
     tb.config(state = DISABLED)
     pp = 1 
    elif bx[0] == '0' and len(bx) == 2:
     clear1()   
     
     tb.config(state = NORMAL)
     tb.insert(END,9)
     tb.config(state = DISABLED)
    elif bx[0] == 'C' or bx[0] == 'U' or bx[0] == 'O' or bx[0] == 'i':
     clear()   
     clearx()
     tb.config(state = NORMAL)
     tb.insert(END,9)
     tb.config(state = DISABLED)     
    elif sign != 'x' and tryy == 1 and num1 == 0 :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,9)
     tb.insert(END,9)
     tb.config(state = DISABLED)
     tryy = tryy +1      
    elif sign != 'x' and tryy == 1  :
     clear()    
     tb.config(state = NORMAL)
     tb.insert(END,9)
     tb.config(state = DISABLED)
     tryy = tryy +1
    else:
        
     tb.config(state = NORMAL)
     tb.insert(END,9)
     tb.config(state = DISABLED)    
    
def typep(*args):
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    if len(bx) >= 26:
     return
    else:
      num1 = tb.get(1.0 , END)
      if '.' not in num1:
       tb.config(state = NORMAL)
       tb.insert(END,'.')
       tb.config(state = DISABLED)
      else:
        pass
    
def typec(*args):
 num1 = tb.get(1.0 , END)
 num1 = float(num1)
 clear()
 tb.config(state = NORMAL)
 if num1 == 0 :
   clearb()
 else: 
  try:
    z = num1*(-1)
  except:
      
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    if bx[0] == 'O':
      pass
    else:
      tb.insert(1.0 , "Overflow")
      tb.config(state = DISABLED)
  z = str(z)
  z1 = z.split(".")
  if z1[1] == '0':
    z = z1[0]
  tb.insert(END , z) 
  tb.config(state = DISABLED)             
                                  
def plus(*args):
 global sign
 global sign1
 global num1
 global tryy
 global pp
 
 numx = tb.get(1.0 , END)
 num1 = float(numx)
 
 sign = "+"
 sign1 = "+"
 tx()
 tryy = 1
 pp = pp + 1
 

def minus(*args):
   
 global sign
 global sign1
 global num1
 global tryy
 global pp 
 numx = tb.get(1.0 , END)
 
 num1 =  float(numx)
 
 sign = "-"
 sign1 = "-"
 tx()
 tryy = 1
 pp = pp + 1

def mul(*args):
   
 global sign
 global sign1
 global num1
 global tryy
 global pp
  
 numx = tb.get(1.0 , END)
 
 num1 =  float(numx)
 
 sign = "*"
 sign1 = "x"
 tx()
 tryy = 1
 pp = pp + 1
 
def div(*args):
   
 global sign
 global sign1
 global num1
 global tryy
 global pp
  
 numx = tb.get(1.0 , END)
 
 num1 =  float(numx)
 
 sign = "/"
 sign1 = "/"
 tx()
 tryy = 1
 pp = pp + 1
 
def roota():
  global sign 
  num1 = tb.get(1.0 , END)
  num1 = float(num1)
  clear()
  clearx()
  
  tb.config(state = NORMAL)
  try:
   z = num1**(1/2)
  except:
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    print(bx)
    if bx[0] == 'O' or bx[0] == 'i':
      tb1.delete(1.0 , END)
    else:
     lock() 
     tb.insert(1.0 , "Overflow")
     tb.config(state = DISABLED)
  z = str(z)
  z1 = z.split(".")
  if len(z1) == 2:
   if z1[1] == '0' and z1[0] != '0' : 
     z = z1[0]
  else:
     z = ".".join(z1)
  tb1.config(state = NORMAL)
  tb1.insert(1.0 , f"√({num1})")
  tb1.config(state = DISABLED)
  tb1.config(state = DISABLED)
  tb.insert(END , z)
  tb.config(state = DISABLED)
  sign = 'x'
  
def cubr():
  global sign 
  num1 = tb.get(1.0 , END)
  num1 = float(num1)
  clear()
  clearx()
  
  tb.config(state = NORMAL)
  try:
   z = num1**(1/3)
  except:
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    print(bx)
    if bx[0] == 'O' or bx[0] == 'i':
      tb1.delete(1.0 , END)
    else:
     lock() 
     tb.insert(1.0 , "Overflow")
     tb.config(state = DISABLED)
  z = str(z)
  z1 = z.split(".")
  if len(z1) == 2:
   if z1[1] == '0' and z1[0] != '0' : 
     z = z1[0]
  else:
     z = ".".join(z1)
  tb1.config(state = NORMAL)
  tb1.insert(1.0 , f"3√({num1})")
  tb1.config(state = DISABLED)
  tb1.config(state = DISABLED)
  tb.insert(END , z)
  tb.config(state = DISABLED)
  sign = 'x'
  
def sqr():
  global sign 
  num1 = tb.get(1.0 , END)
  num1 = float(num1)
  clear()
  clearx()
  tb.config(state = NORMAL)
  try:
   z = num1**2
  except:
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    if bx[0] == 'O':
      pass
    else:
     lock() 
     tb.insert(1.0 , "Overflow")
     tb.config(state = DISABLED)
     
  zx = str(z)
  z1 = zx.split(".")
  
  if len(z1) == 2:
   if z1[1] == '0' and z1[0] != '0' :
     z = z1[0]
   else:
     z = ".".join(z1)    
  tb1.config(state = NORMAL)
  tb1.insert(1.0 , f"sqr({num1})")
  tb1.config(state = DISABLED)   
  tb.insert(END , z)
  tb.config(state = DISABLED)
  sign = 'x'
 
  
def cub():
  global sign 
  num1 = tb.get(1.0 , END)
  num1 = float(num1)
  clear()
  clearx()
  tb.config(state = NORMAL)
  try:
   z = num1**3
  except:
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    if bx[0] == 'O':
      pass
    else:
     lock() 
     tb.insert(1.0 , "Overflow")
     tb.config(state = DISABLED)
     
  zx = str(z)
  z1 = zx.split(".")
  
  if len(z1) == 2:
   if z1[1] == '0' and z1[0] != '0' :
     z = z1[0]
   else:
     z = ".".join(z1)    
  tb1.config(state = NORMAL)
  tb1.insert(1.0 , f"cub({num1})")
  tb1.config(state = DISABLED)   
  tb.insert(END , z)
  tb.config(state = DISABLED)
  sign = 'x'
      
def inv():
  global sign 
  num1 = tb.get(1.0 , END)
  num1 = float(num1)
  z = num1
  
  clear()
  clearx()
  tb.config(state = NORMAL)
  try:
   z = num1**(-1)
  except:
    
    tb.config(state = NORMAL)
    b = tb.get(1.0 , END)
    b1 = str(b)
    bx = list(b1)
    if bx[0] == 'O':
      pass
    else:
     lock() 
     tb.insert(1.0 , "INFINITY")
     tb.config(state = DISABLED)
     
     
  z = str(z)
  z1 = z.split(".")
  if z1[1] == '0':
    z = z1[0]
  tb1.config(state = NORMAL)
  tb1.insert(1.0 , f"inv({num1})")
  tb1.config(state = DISABLED)            
  tb.insert(END , z)
  tb.config(state = DISABLED)
  sign = 'x'    
 
 #MAIN FUNCTION::::::: STARTED
  
def eua(*args):
  global num2
  global num1
  global sign
  global sign2
  global z
  global px
  global pill
  global con
  global pp
  
  pp = 0
  sign2 = '=' 
  con = num1
  if px == 1:
   num2 = tb.get(1.0 , END)
   num2 = float(num2)
  else:
    num2 =  pill
  
  p = tb1.get(1.0 , END)
  p = str(p)
  p1 = list(p)
  
  #PLUS OPERATOR:STARTED
  if sign == "+":
    clear()# clearing Field
    tb.config(state = NORMAL)
    try:
     z = num1+num2
    except:
      tb.config(state = NORMAL)
      b = tb.get(1.0 , END)
      b1 = str(b)
      bx = list(b1)
      if bx[0] == 'O':
        pass
      else:
       lock() 
       tb.insert(1.0 , "Overflow")
       tb.config(state = DISABLED)
     
    z = str(z)
    z1 = z.split(".")
    if len(z1) == 2:
     if z1[1] == '0' :
      z = z1[0]
    else:
      z = z1[0]  
    
    
    tb.insert(END , (z))
    tb.config(state = DISABLED)
    num1 = 0
    sign = "x"
    if '+' in p1:
     sign = "+"
     num1 = float(z)
     pill = num2
     px = px + 1
    else:
       sign = "x"
       num1 = 0
       num2 = 0
       px = 1
    ty()
    
  #PLUS OPERATOR:ENDED
  
  #MINUS OPERATOR:STARTED   
  elif sign == "-":
    clear()# clearing Field
    tb.config(state = NORMAL)
    try:
     z = num1-num2
    except:
      tb.config(state = NORMAL)
      b = tb.get(1.0 , END)
      b1 = str(b)
      bx = list(b1)
      if bx[0] == 'O':
        pass
      else:
       lock() 
       tb.insert(1.0 , "Overflow")
       tb.config(state = DISABLED)
     
    z = str(z)
    z1 = z.split(".")
    if len(z1) == 2:
     if z1[1] == '0' :
      z = z1[0]
    else:
      z = z1[0]  
    
    
    tb.insert(END , (z))
    tb.config(state = DISABLED)
    num1 = 0
    sign = "x"
    if '-' in p1:
     sign = "-"
     num1 = float(z)
     pill = num2
     px = px + 1
    else:
       sign = "x"
       num1 = 0
       num2 = 0
       px = 1
    ty()
  #MINUS OPERATOR:ENDED
    
  #MULTIPLY OPERATOR:STARTED  
  elif sign == "*":
    clear()# clearing Field
    tb.config(state = NORMAL)
    try:
     z = num1*num2
    except:
    
      tb.config(state = NORMAL)
      b = tb.get(1.0 , END)
      b1 = str(b)
      bx = list(b1)
      if bx[0] == 'O':
        pass
      else:
       lock() 
       tb.insert(1.0 , "Overflow")
       tb.config(state = DISABLED)
     
    z = str(z)
    z1 = z.split(".")
    if len(z1) == 2:
     if z1[1] == '0' :
      z = z1[0]
    else:
      z = z1[0]  
    
    tb.insert(END , (z))
    tb.config(state = DISABLED)
    num1 = 0
    sign = "x"
    if 'x' in p1:
     sign = "*"
     num1 = float(z)
     pill = num2
     px = px + 1
    else:
       sign = "x"
       num1 = 0
       num2 = 0
       px = 1
    ty()
  #MULTIPLY OPERATOR:ENDED
  
  #DIVISOR OPERATOR:STARTED  
  elif sign == "/":
    clear()# clearing Field
    tb.config(state = NORMAL)
    if num1 == 0 and num2 ==0:
     lock() 
     tb.config(font = ("Times",25), wrap = "word") 
     tb.insert(END , "Undefined result")
     tb.config(state = DISABLED)  
     
    elif num2 == 0:
     lock() 
     tb.config(font = ("Times",25), wrap = "word") 
     tb.insert(END , "Can not divide by zero")
     tb.config(state = DISABLED)
     
    else:  
     try: 
      z = num1/num2
     except:
    
        tb.config(state = NORMAL)
        b = tb.get(1.0 , END)
        b1 = str(b)
        bx = list(b1)
        if bx[0] == 'O' :
          pass
        else:
         lock() 
         tb.insert(1.0 , "Overflow")
         tb.config(state = DISABLED)
         
     
     z = str(z)
     z1 = z.split(".")
     if len(z1) == 2:
      if z1[1] == '0' :
       z = z1[0]
     else:
       z = z1[0]  
     
     tb.insert(END , (z))
     tb.config(state = DISABLED)
     num1 = 0   
     sign = "x"
    if '/' in p1:
     sign = "/"
     num1 = float(z)
     pill = num2
     px = px + 1
    else:
       sign = "x"
       num1 = 0
       num2 = 0
       px = 1
    ty()
     #DIVISOR OPERATOR:ENDED 
     
     #MAIN FUNCTION ::::: ENDED

def quit(*args):
  root.destroy()            
 

 
 
 
      
style1 = ttk.Style()
style = ttk.Style()




style.configure('TButton', font = ('Times', 20, 'bold'),foreground = 'BLACK',background = 'WHITE',width = 4 , padding = 8)
style1.configure('W.TButton', font = ('Times', 20, 'bold'),foreground = 'RED',background = 'WHITE',width = 4 , padding = 8)



#NUMBER BUUTONS:- STARTED

but0 = ttk.Button(f2 , text = "   0   " , style = 'T.TButton',command = type0)
but0.place(x = 80,y =  266)



but1 = ttk.Button(f2 , text = "   1   " , style = 'T.TButton',command = type1)
but1.place(x = 00,y =  212)



but2 = ttk.Button(f2 , text = "   2   " , style = 'T.TButton',command = type2)
but2.place(x = 80,y =  212)



but3    = ttk.Button(f2 , text = "   3   " , style = 'T.TButton',command = type3)
but3.place(x = 160,y =  212)


but4 = ttk.Button(f2 , text = "   4   " , style = 'T.TButton', command = type4)
but4.place(x = 0,y =  158)


but5 = ttk.Button(f2 , text = " 5 " , style = 'T.TButton', command = type5)
but5.place(x = 80,y =  158)


but6 = ttk.Button(f2 , text = "   6   " ,style = 'T.TButton', command = type6)
but6.place(x = 160,y =  158)



but7 = ttk.Button(f2 , text = "   7   " , style = 'T.TButton',command = type7)
but7.place(x = 0,y =  104)


but8 = ttk.Button(f2 , text = "   8   " , style = 'T.TButton',command = type8)
but8.place(x = 80,y =  104)


but9 = ttk.Button(f2 , text = "   9   " , style = 'T.TButton',command = type9)
but9.place(x = 160,y =  104)

#NUMBER BUUTONS:- ENDED

#FUNCTIONAL BUUTONS:- STARTED

butplus = ttk.Button(f2 , text = "  +/-  " ,  style = 'T.TButton', command = typec)
butplus.place(x = 0,y =  266)

butd = ttk.Button(f2 , text = "   .   " ,  style = 'T.TButton', command = typep)
butd.place(x = 160,y =  266)

butdi = ttk.Button(f2 , text = "   /    " ,  style = 'T.TButton', command = div)
butdi.place(x = 240 ,y =  266)

butm = ttk.Button(f2 , text = "   -    " ,  style = 'T.TButton', command = minus)
butm.place(x = 240,y =  158)

butp = ttk.Button(f2 , text = "   +    " ,  style = 'T.TButton', command = plus)
butp.place(x = 240,y =  212)

butmi = ttk.Button(f2 , text = "   x    " ,  style = 'T.TButton', command = mul)
butmi.place(x = 240,y =  104)

bute = ttk.Button(f2 , text = "   =    " ,  style = 'T.TButton', command = eua)
bute.place(x = 240,y =  52)

butr = ttk.Button(f2 , text = "√" ,  style = 'T.TButton', command = roota)
butr.place(x = 160,y =  52)

bclear = ttk.Button(f2 , text = "CE" ,  style = 'W.TButton', command = clearb)
bclear.place(x = 0,y =  0)

bclear1 = ttk.Button(f2 , text = " C " ,  style = 'T.TButton', command = clear1b )
bclear1.place(x = 80,y =  0 )

bc1 = ttk.Button(f2 , text = " ∛ " ,  style = 'T.TButton', command = cubr )
bc1.place(x = 240,y =  0)

bc2 = ttk.Button(f2 , text = " x² " ,  style = 'T.TButton', command = sqr )
bc2.place(x = 80,y =  52)

bc3 = ttk.Button(f2 , text = " x³ " ,  style = 'T.TButton', command = cub )
bc3.place(x = 160,y =  0)

bc4 = ttk.Button(f2 , text = " 1/x " ,  style = 'T.TButton', command = inv )
bc4.place(x = 0,y =  52)

#FUNCTIONAL BUUTONS:- ENDED

root.bind("<Return>" , eua )
root.bind("<BackSpace>" , clear1b )
root.bind("<Delete>" , clearb )
root.bind("0" , type0 )
root.bind("1" , type1 )
root.bind("2" , type2 )
root.bind("3" , type3 )
root.bind("4" , type4 )
root.bind("5" , type5 )
root.bind("6" , type6 )
root.bind("7" , type7 )
root.bind("8" , type8 )
root.bind("9" , type9 )

root.bind("/" , div )
root.bind("d" , div )
root.bind("D" , div )

root.bind("x" , mul )
root.bind("X" , mul )
root.bind("*" , mul )

root.bind("=" , plus )
root.bind("a" , plus )
root.bind("A" , plus )
root.bind("+" , plus )

root.bind("-" , minus )
root.bind("s" , minus )
root.bind("S" , minus )

root.bind("." , typep )

root.bind("<Escape>" , quit )

root.bind("z" , typec )
root.bind("Z" , typec )


root.mainloop()