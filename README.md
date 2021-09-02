# JAM-College-Predictor
### About model
The model predicts the college that a Jam aspirant can get based on his All India Rank(AIR).<br>
The model has been trained on the cutoffs of previous years,its works fine for standard ranks in the range of 1-1500, but might not be reliable beyond this.<br>
You can use this model to get a hint of what institute you might get based on your rank.

### Data Gathering
The data has been gathered from the various Closing and Opening ranks released by the respective IITs hosting the IIT Jam Councelling.
<br>
All the excel files has been included in this repository.

### Model Creation
Different models have been created for the different castes(like General,OBC,etc) using a pipeline in which I have used Column Transformer to transform both the categorical
and the Numerical columns using One Hot encoding and Standard Scalar in just one go.
<br>
<br>
![Hnet com-image(1)](https://user-images.githubusercontent.com/40202640/131882224-52894a66-3faf-4660-bae8-f33237e9ef32.gif)








The model has been hosted on Heroku Platform 
Model link :- https://jam-college-predictor.herokuapp.com 
<br>
Youtube link :- https://www.youtube.com/watch?v=pvaKRrik69o
























