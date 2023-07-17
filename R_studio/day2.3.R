
# Create a function to generate random scores
generate_scores <- function() {
  scores <- round(runif(3, min = 0, max = 100))
  return(scores)
}

# Create a matrix for the students' scores
students <- c("Ali", "Badur", "Mohammed", "Said", "Saif")
scores_matrix <- matrix(0, nrow = length(students), ncol = 3)
colnames(scores_matrix) <- c("Math", "Phys", "Bio")
rownames(scores_matrix) <- students
scores_matrix

# Fill in the matrix with scores
for (i in 1:length(students)) {
  scores_matrix[i, ] <- generate_scores()
}

# add colums name totat and calculate it for each students:
scores_matrix = cbind(scores_matrix,'Total'=(rowSums(scores_matrix)))
scores_matrix = cbind(scores_matrix,'Percent'=(rowSums(scores_matrix)))
scores_matrix

scores_matrix = rbind(scores_matrix,'Total'=(colSums(scores_matrix)))
scores_matrix

scores_matrix=edit(scores_matrix)

#--------------------------------------------------------
mydf=data.frame(scores_matrix)
mydf

library(xlsx)
df <- data.frame(matrix())
write.xlsx(mydf,"scores.xlsx")



