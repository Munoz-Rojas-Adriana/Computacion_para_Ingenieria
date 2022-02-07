mayornota = float();
A = [ [ [2, 2.4, 3.2], [3.5, 3, 3.2], [4.2, 5, 4.6] ] ];

for i in range(0, 1):
    
      sumanotas = 0;
      
      for j in range(0, 3):
          
          acumulador = 0;
          
          for k in range(0, 3):
              acumulador = acumulador + A[i][j][k];
              
         
          sumanotas = sumanotas + (acumulador / 3);    
          
          print("promedio de notas del curso: " + str(j+1) + " > " + str(acumulador / 3));
          
          if((sumanotas / 3) > mayornota):
              mayornota = sumanotas / 3;
              
      print("\npromedio de notas por curso: " + str(sumanotas / 3));
      print("el mayor promedio de notas de los cursos es: " + str(mayornota));