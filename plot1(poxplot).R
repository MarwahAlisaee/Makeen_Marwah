# creat value 
set.seed(123)
rnorm(20,3,4)
rnorm(20,5,2)*10
var1=rnorm(100,50,3)
var1[3]=var1[3]+40
var1[3]=var1[3]+50
boxplot(-c(3,50))
boxplot(var1, horizontal=TRUE, col="blue")
title(main = list("var1", cex=1.5,col="red"))
fivenum(var1)
summary(var1)
?rnorm
