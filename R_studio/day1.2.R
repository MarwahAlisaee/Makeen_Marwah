library(readr)
marksheet <- read_csv("C:/Users/Marwah/Downloads/marksheet.csv")
View(marksheet)

#-----------------------------------------

mymatrix=matrix(1:9, nrow = 3, ncol=3)
mydf=data.frame(mymatrix)
mydf

#---------------------------------------------

library(xlsx)
df <- data.frame(matrix(1:10))
write.xlsx(mydf,"output.xlsx")

#-----------------------------------------------

library(rio)
export(mtcars,"mtcars1.csv")

#------------------------------------------------




