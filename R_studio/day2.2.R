df=mtcars
str(df)
summary(df)

hist(df$mpg, col="red", main="Code Academe")
?hist

#---------------------------------------------------
library(ggplot2)
varnorm=as.integer(rnorm(200,4,3))
varunif=as.integer(runif(200,1,7))
Count =rnorm(200,10,5)
df=data.frame(varnorm, varunif,Count)
hist(varnorm)

ggplot2(data=df, aes(varnorm))+gerom_histogram()
