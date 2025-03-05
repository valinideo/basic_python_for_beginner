# simple code to find dot producuct of two list
x= [12,25,45,85,95,65,45,1]
y= [45,85,95,65,45,1,0,51]
# dot_product = x[0]*y[0] + x[1]*y[1] + x[2]*y[2] + x[3]*y[3] + x[4]*y[4] + x[5]*y[5] + x[6]*y[6] + x[7]*y[7]
# dot_product= 12*45 + 25*85 + 45*95 + 85*65 + 95*45 + 65*1 + 45*0 + 1*51
dot_product = 0
for i in range(len(x)):
   dot_product += x[i] * y[i]
print(dot_product)
