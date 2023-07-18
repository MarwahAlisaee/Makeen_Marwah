mean1<- function(data) {
  value <- mean(data)
  return(value)
}

sd1<- function(data) {
  value <- sd(data)
  return(value)
}


mydata <- c(1, 2, 3, 4, 5,7)
mean_r <- mean1(mydata)
sd_r <- sd1(mydata)

myfunction=function(var1){
  print(mean(var1))
  print(sd(var1))
}

myfunction(c(7:9))
print(mean_r)  
print(sd_r) 

#--------------------------------------------------------------------------------

