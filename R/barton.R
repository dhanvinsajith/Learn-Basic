#INTRODUCTION AND PACKAGES
'library(datasets)
head(iris)
plot(iris)
dev.off()
install.packages("pacman")
library("pacman")
library(pacman)
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)
p_unload(all)
detach("package:datasets", unload = TRUE)'


#PLOT()
'
library(datasets)
head(iris)
?head #help on command
?plot
plot(iris$Species)
plot(iris$Petal.Length)
plot(iris$Species, iris$Petal.Length)
plot(iris$Petal.Length, iris$Petal.Width)
plot(iris)
plot(iris$Petal.Length, iris$Petal.Width,
    col = "#cc0000",
    pch = 19,
    main = "IRIS: Petal Length vs Petal Width",
    xlab = "Petal Length",
    ylab = "Petal Width")
plot(cos, 0, 2*pi) #cosine
plot(exp, 1, 5) #exponential distribution
plot(dnorm, -3, +3) #density of normal distribution
plot(dnorm, -3, +3,
    col = "#cc0000",
    lwd = 5,
    main = "Standard Normal Distribution",
    xlab = "z-scores",
    ylab = "Density")
detach("package:datasets", unload = TRUE)
'


#BAR GRAPHS
'
library(datasets)
?mtcars
head(mtcars)
barplot(mtcars$cyl)
cylinders <- table(mtcars$cyl)
barplot(cylinders)
plot(cylinders) #easier with bar chart
detach("package:datasets", unload = TRUE)
'

#HISTOGRAMS
'
library(datasets)
?iris
head(iris)
hist(iris$Sepal.Width)
hist(iris$Sepal.Length)
hist(iris$Petal.Length)
hist(iris$Petal.Width)
par(mfrow = c(3, 1)) #change parameter with combination of 3 rows, 1 column -> similar to tuples
hist(iris$Petal.Width [iris$Species == "setosa"], #for setosa
     xlim = c(0, 3),
     breaks = 9,
     main = "Petal Widths for Setosa",
     xlab = "",
     col = "red")
hist(iris$Petal.Width [iris$Species == "versicolor"], #for versicolor
     xlim = c(0, 3),
     breaks = 9,
     main = "Petal Widths for Versicolor",
     xlab = "",
     col = "green")
hist(iris$Petal.Width [iris$Species == "virginica"], #for virginica
     xlim = c(0, 3),
     breaks = 9,
     main = "Petal Widths for Virginica",
     xlab = "",
     col = "blue")
par(mfrow = c(1, 1)) #change graphical layout back
detach("package:datasets", unload = TRUE)
'

#SCATTERPLOTS
'
library(datasets)
?mtcars
head(mtcars)
hist(mtcars$wt)
hist(mtcars$mpg)
plot(mtcars$wt, mtcars$mpg)
plot(mtcars$wt, mtcars$mpg,
     pch = 19, #solid circle (point character)
     cex = 1.5, #size of things (150%)
     col = "#40e0d0",
     main = "MPG as a function of weight of the cars",
     xlab = "Weight (in 1000 lbs)",
     ylab = "Miles Per Gallon")
detach("package:datasets", unload = TRUE)
'


#OVERLAYING PLOTS
'
library(datasets)
?lynx
head(lynx)
hist(lynx)
hist(lynx,
     breaks = 14, #suggests 14 bins
     freq = FALSE, #shows density not frequency
     col = "thistle1",
     main = paste("Histogram of Annual Canadian Lynx",
                  "Trappings, 1821-1934"),
     xlab = "Lynx Trapped")
curve(dnorm(x, mean = mean(lynx), sd = sd(lynx)),
            col = "thistle4",
            lwd = 2,
            add = TRUE) #dnorm is density of normal distribution
lines(density(lynx), col = "blue", lwd = 2)
lines(density(lynx, adjust = 3), col = "purple", lwd = 2)
rug(lynx, lwd = 2, col = "gray")
detach("package:datasets", unload = TRUE)
'

#SUMMARY() and DESCRIBE()
'
library(datasets)
head(iris)
summary(iris$Species)
summary(iris$Sepal.Length)
summary(iris)
library(pacman)
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)
p_load(psych)
p_help(psych, web=F)
describe(iris$Sepal.Length) #describe() is much more detailed than summary()
describe(iris)
detach("package:datasets", unload = TRUE)
p_unload(all)
detach("package:pacman", unload = TRUE)
'

#SELECTING CASES
'
library(datasets)
head(iris)
hist(iris$Petal.Length)
summary(iris$Petal.Length)
summary(iris$Species)
#selecting by category
par(mfrow = c(3, 1))
hist(iris$Petal.Length[iris$Species == "versicolor"],
     main = "Petal Length - Versicolor")
hist(iris$Petal.Length[iris$Species == "virginica"],
     main = "Petal Length - Virginica")
hist(iris$Petal.Length[iris$Species == "setosa"],
     main = "Petal Length - Setosa")
par(mfrow = c(1, 1))
#selecting by value(quantitative)
hist(iris$Petal.Length[iris$Petal.Length < 2],
     main = "Lengths < 2")
#multiple cases
hist(iris$Petal.Length[iris$Species == "virginica" & iris$Petal.Length < 5.5],
     main = "Petal Length < 5.5 - Virginica",
     xlab = "Petal Length")
#create new dataset with subsample
i.setosa <- iris[iris$Species == "setosa",]
head(i.setosa)
summary(i.setosa$Petal.Length)
rm(list = ls())
detach("package:datasets", unload = TRUE)
'

#DATA FORMATTING
'
#numeric
n1 <- 15 #double by default
n1
typeof(n1)

#character
c1 <- "c"
c1
typeof(c1)

#string
c2 <- "st4ring of text"
c2
typeof(c1)

#logical
l1 <- TRUE
l1
typeof(l1)
l2 <- F #abbreviated
l2

#vector
v1 <- c(1, 2, 3, 4, 5) #c stands for concatenate
v1
is.vector(v1)

#matrix
m1 <- matrix(c(T, T, F, F, T, F), nrow = 2)
m1
m2 <- matrix(c("a", "b", #formatting rows matrix
               "c", "d"),
             nrow = 2,
             byrow = T)
m2

#array
a1 <- array(c(1:24), c(4, 3, 2))
a1

#data frame
vNum <- c(1, 2, 3)
vChar <- c("a", "b", "c")
vLog <- c(T, F, T)
dfa <- cbind(vNum, vChar, vLog) #changes everything to character type
df <- as.data.frame(cbind(vNum, vChar, vLog)) #maintains datatypes
df


#list
o1 <- c(1, 2, 3)
o2 <- c("a", "b", "c", "d")
o3 <- c(T, F, T, T, F)
list1 <- list(o1, o2, o3)
list1
list2 <- list(o1, o2, o3, list1)
list2

#coercing types
(coerce1 <- c(1, "b", TRUE))
typeof(coerce1)

#coercing to integer
(coerce2 <- 5)
typeof(coerce2)
(coerce3 <- as.integer(5))
typeof(coerce3)
(coerce4 <- c("1", "2", "3"))
typeof(coerce4)
(coerce5 <- as.numeric(c("1", "2", "3")))
typeof(coerce5)

#coerce matrix to dataframe
(coerce6 <- matrix(1:9, nrow = 3))
is.matrix(coerce6)
(coerce7 <- as.data.frame(matrix(1:9, nrow = 3)))
is.data.frame(coerce7)
'

#FACTORS
'
(x1 <- 1:3)
(y <- 1:9)
(df1 <- cbind.data.frame(x1, y)) #combining
typeof(df1$x1)
str(df1) #structure
(x2 <- as.factor(c(1:3)))
(df2 <- cbind.data.frame(x2, y))
typeof(df2$x2)
str(df2)
#define existing variable as a dataframe
x3 <- c(1:3)
df3 <- cbind.data.frame(x3, y)
(df3$x3 <- factor(df3$x3,
                  levels = c(1, 2, 3)))
typeof(df3$x3)
str(df3)
#labels
x4 <- c(1:3)
df4 <- cbind.data.frame(x4, y)
df4$x4 <- factor(df4$x4,
                 levels = c(1, 2, 3),
                 labels = c("macOS", "Windows", "Linux"))
df4
typeof(df4$x4)
str(df4)
#ordered factors
x5 <- c(1:3)
df5 <- cbind.data.frame(x5, y)
df5
(df5$x5 <- ordered(df5$x5,
                   levels = c(3, 1, 2),
                   labels = c("No", "maybe", "Yes")))
df5
typeof(df5$x5)
str(df5)

rm(list = ls()) #clean environment
'

#ENTERING DATA
'
# <- is the assignment operator in R
# It is read as "gets"
# It can go both ways

x1 <- 1:10
x1

x2 <- 10:1 #descending
x2

(x3 <- seq(10))#easier
(x4 <- seq(30, 0, by = -3)) #step size


#concatenate
?c
x5 <- c(5, 4, 1, 6, 7, 8, 2, 3, 3, 3, 5, 2)
x5

#scan
?scan
x6 <- scan()
#enter values in console
x6

#rep (repetition)
?rep
x7 <- rep(TRUE, 5)
x7
x8 <- rep(c(TRUE, FALSE), 5) #repeat set
x8
x9 <- rep(c(TRUE, FALSE), each = 5) #repeat set in order one element after the other
x9

rm(list = ls()) #clean environment
'

#IMPORTING DATA
'
#rio (R Input Output) is a very useful dataset when importing data

pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)

rio_csv <- import("C:/Users/dange/OneDrive/Desktop/learn/R/ImportingData_Datasets/mbb.csv")
head(rio_csv)
rio_txt <- import("C:/Users/dange/OneDrive/Desktop/learn/R/ImportingData_Datasets/mbb.txt")
head(rio_txt)
rio_xlsx <- import("C:/Users/dange/OneDrive/Desktop/learn/R/ImportingData_Datasets/mbb.xlsx")
head(rio_xlsx)

?View
View(rio_csv)

r_txt1 <- read.table("C:/Users/dange/OneDrive/Desktop/learn/R/ImportingData_Datasets/mbb.txt",
                     header = TRUE,
                     sep = "\t")
head(r_txt1)
detach("package:pacman", unload = TRUE)
'

#HIERARCHICAL CLUSTERING
'
library(datasets)
head(mtcars)
cars <- mtcars[, c(1:4, 6:7, 9:11)]
head(cars)
hc <- cars %>% #get cars data
  dist %>%     #compute distance/dissimilarity matrix
  hclust       #computer hierarchical clusters
plot(hc)
rect.hclust(hc, k = 2, border = "gray")
rect.hclust(hc, k = 3, border = "blue")
rect.hclust(hc, k = 4, border = "green4")
rect.hclust(hc, k = 5, border = "darkred")

rm(list = ls()) #clean environment
detach("package:datasets", unload = TRUE)
'

#PRINCIPAL COMPONENTS (dimensionality reduction)
'
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)
library(datasets)

head(mtcars)
cars <- mtcars[, c(1:4, 6:7, 9:11)]
head(cars)

pc <- prcomp(cars,
             center = TRUE,
             scale = TRUE)
summary(pc)
plot(pc)
pc
predict(pc) %>% round(2)
biplot(pc)

rm(list = ls()) #clean environment
detach("package:datasets", unload = TRUE)
'

#REGRESSION
'
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)
library(datasets)
?USJudgeRatings
head(USJudgeRatings)
data <- USJudgeRatings

x <- as.matrix(data[-12])
y <- data[, 12]

reg1 <- lm(y ~ x)
#or you could do it this way
reg1 <- lm(RTEN ~ CONT + INTG + DMNR + DILG + CFMG + DECI + PREP + FAMI + ORAL + WRIT + PHYS,
         data = USJudgeRatings)

reg1
summary(reg1)

anova(reg1) #coefficients with inferential tests
coef(reg1)  #coefficients
confint(reg1) #confidence interval for coefficients
resid(reg1)  #residuals case by case
hist(residuals(reg1))  #histogram of residuals

rm(list = ls()) #clean environment
detach("package:datasets", unload = TRUE)
detach("package:pacman", unload = TRUE)
'

#ADDITIONAL MODELS
'
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)
library(datasets)
p_load(lars, caret)

data <- USJudgeRatings
x <- as.matrix(data[-12])
y <- data[, 12]

stepwise <- lars(x, y, type = "stepwise") #convetional stepwise regression

forward <- lars(x, y, type = "forward.stagewise") #like stepwise but better generalizability

lar <- lars(x, y, type = "lar") #least angle regression

lasso <-  lars(x, y, type = "lasso") #least abs shrinkage and selection operator

r2comp <- c(stepwise$R2[6], forward$R2[6], #comparison of R^2 values
            lar$R2[6], lasso$R2[6]) %>%
            round(2)
names(r2comp) <- c("stepwise", "forward", "lar", "lasso")
r2comp

rm(list = ls()) #clean environment
detach("package:datasets", unload = TRUE)
detach("package:pacman", unload = TRUE)
'



















