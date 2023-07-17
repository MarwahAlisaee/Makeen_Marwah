# Day 1 coding 
x <- 'r'
class(x)
x= c('r','t')
x1= c(3.5,45)
c(TRUE,FALSE)->X2
#--------------------------------------------
  
temp= c(27,71,68,73,69,75,71)
temp
length(temp)
names(temp)=c('Sun','Mon','Tue','Wen','Thr','Fri','Sat')
temp[c(3:6)]
# Square temp
Square_temp=sqrt(temp)
Square_temp
# Multply by 4
Multply=temp*4
Multply
# Add 10
add=temp+10
add
# min
min(temp)
# max
max(temp)
# median
median(temp)

#------------------------------------------
temp[temp>50]
temp[(temp>80 | temp<40)]

temp70 =temp[temp>69 &temp<80]
temp70

temp70 =temp[temp !=(temp>69 &temp<80)]
temp70

tempNo70 =temp[temp<70 | temp>79]
tempNo70

temp['Fri']

mean(temp[c('Fri','Sat')])

temp01 =temp[!names(temp)%in% c('Mob','Tus')]
temp01

#-----------------------------------------------------------

#Q1: what is two to the power of five
a= 2**5
a

#Q2: Create a vactor called stock.price with the following datd point :23,27,23,21,34
stock=c(23,27,23,21,34)
stock
  
#Q3: Assing names to the price data points related to the days started with mon, tus,...
names(stock)=c('Mon','Tue','Wen','Thr','Fri')
stock

#Q4: average mean of (stock) :
mean(stock)

#Q5: Create vactor called over.23 consisting of logecals that correspoond
#to the days where the stock was more than $23
over.23=stock>23
over.23

#Q6:Use the fillter:
over.23=stock[stock>23]
over.23

#Q7: higest  days 
max(stock)
stock[stock==max(stock)]
names(stock[stock==max(stock)])
names(stock[stock==min(stock)])

#----------------------------------------------------
# how to use matrix:

y <- matrix(1:20, nrow=5, ncol=4)
y

calls <- c(1,26,24,68)
rnames <- c("R1", "R2")
cnames <- c("c1", "c2")
mymatrix <- matrix(calls, nrow=2, ncol = 2, byrow = TRUE,
                   dimnames=list(rnames,cnames))
mymatrix
mymatrix*mymatrix

help("matrix")
#----------------------------------------------------

a <- matrix(1:10, nrow = 2, ncol= 3)
a
b <- matrix(1:10, nrow = 3, ncol= 2)
b

c=a%*%b
c

#-----------------------------------------------------

a[1,2]
b[2,2]
a[,3]
a[2,]


