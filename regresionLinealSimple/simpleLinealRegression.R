#Regresion lineal
dataset=read.csv("Salary_Data.csv")

library(caTools)
set.seed(123)
split=sample.split(dataset$Salary,SplitRatio = 2/3)
training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)
#ajustar el modelo Regresion Lineal Simple en el conjunto entrnamiento
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#Predecir el resultado con el conjunto de test
#'la funcion predic funciona por que las columas 
#'del conjunto de ttraining y testing se llaman igual
#'si no fuese asi no funcionaria'#
y_pred=predict(regressor,testing_set)
#visualizacion de datos en conjunto de entrenamiento
#´install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),
             colour="red") +
  geom_line(aes(training_set$YearsExperience,y=predict(regressor,training_set)),color="blue") +
  ggtitle("Sueldo vs Años de Experiencia(conjunto de Entrenamiento)") +
  xlab("Años de Experiencia") + ylab("Sueldo en ($)")
#visualizacion de datos en conjunto de testing
ggplot() +
  geom_point(aes(x=testing_set$YearsExperience,y=testing_set$Salary),
             colour="red") +
  geom_line(aes(training_set$YearsExperience,y=predict(regressor,training_set)),color="blue") +
  ggtitle("Sueldo vs Años de Experiencia(conjunto de Testing)") +
  xlab("Años de Experiencia") + ylab("Sueldo en ($)")

  
