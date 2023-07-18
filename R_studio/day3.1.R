df1 <- data.frame(c('ID', 'Name', 'prc'))
df1<- edit(df1)

df1 <- data.frame(cbind('ID', 'Name', 'prc'))
df1<- edit(df1)

df1 <- data.frame(cbind('ID', 'Name', 'prc'))
df1<- edit(df1)
df1<- edit(df1)

view(df1)
names(df1)=c('ID', 'Name', 'prc')
view(df1)


df2=data.frame(cbind('ID'=5))
view(df2)

df2=data.frame(cbind('ID'=2, 'status'='Enrolled', 'Year'=4))

# this is other selution:

ID=c(1:3)
Name= c('Ali','Said','Ahmed')
prc=c(87,99,81)

df1=data.frame('ID'=ID, 'Name'=Name, 'prc'=prc)
df1

df2=data.frame(
  'ID'=c(2:5),
  'status'=c('Grd','Grd','Enr','Enr'),
  'Year'=c(3,5,2,1)
)
df2
# Merge data frame: 
total <- merge(df1,df2, by='ID')
total

#------------------------------------------------------------------------------------------

# selection Observation 
mydata=data.frame(Titanic)
mydata
head(mydata)

newdata <- mydata[which(mydata$Class=='Crew' & mydata$Survived=='Yes'),]
newdata

# the subset()
newdata <- subset(mydata, mydata$Class=='Crew' & mydata$Survived=='Yes', select =c(Class,Survived))
newdata

newdata <- subset(mydata, mydata$Class=='Crew' & mydata$Survived=='Yes', mydata$Age=='Child')
newdata

#Random Samples
mysample <- mydata[sample(1:nrow(mydata),3, replace = FALSE),]
mysample

# Using SQL statment to mamipulate data frame
library(sqldf)
newdf <- sqldf("select * from mtcars where carb=1 order by mpg", row.names =TRUE )
newdf

#----------------------------------------------------------------------------------------------------

GPA <- 190

if(GPA <100 & GPA>90){
  print("A")
}else if (GPA <90 & GPA>80){
  print("B")
}else if (GPA <80 & GPA>70){
  print("C")
}else if (GPA <70 & GPA>60){
  print("D")
}else if (GPA <60 & GPA>0){
  print("F")
}else{
  print("enter correct GPA")
}
 

#--------------------------------------------------------------------------------

s= as.integer(readline(prompt = "Enter Start num: "))
e= as.integer(readline(prompt = "Enter Start num: "))
i=s
sum=0
while(i<=e){
  sum=sum+1
  i=i+1
}
 print(paste("Sum is ", sum))

 #-------------------------------------------------------------------------
mat <- matrix(1:25, nrow = 5)
mat

for (i in mat){
  print(i)
}

 for (row in 1:nrow(mat)){
   for (col in 1:ncol(mat)) {
     print(paste('The element at raw: ',row, 'and col: ', col, 'is ', mat[row,col]))
     
   }
 }
#--------------------------------------------------------------------------------------

# write functions to find main and sd of numeric variable in 

mean <- function(data) {
  value <- mean(data)
  return(value)
}

sd <- function(data) {
  value <- sd(data)
  return(value)
}


mydata <- c(1, 2, 3, 4, 5,7)
mean_r <- mean(mydata)
sd_r <- sd(mydata)


print(mean_r)  
print(sd_r) 

 