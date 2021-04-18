## Traffic-Signal-Recognition
Traffic Signal Recognition recognizes and classifies road signal images into any one of 43 different classes that are used worldwide


Web-API: 

![Sample Web api](https://github.com/Devil-Echo/Traffic-Signal-Recognition/blob/main/figures/sample.png)


[Link to dataset](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)


*How to use* : 
- Download the dataset from Kaggle using the link given above.
- Unzip the contents, you will get 3 folders and 3 csv files.
- Create similar folder/file structure as in the github repository.
- Copy the contents of the 'train' folder from the unzipped version to your local machine.
- Similarly, copy the contents of the 'Test' folder to 'static/Test/' in your machine. (Check relative path in repo for reference screenshot).
- Finally, open Anaconda command propmpt or cmd/powershell if you are using standalone python and run ->
```
python web-app.py
```
Open any browser and  type -> `localhost:4000` in the url bar.
The web app will start, to classify new 'sign images', move these images to '/static/Test/' directory in the project folder
else the image will not render on the webpage, though it will be classified.
