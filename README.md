# HNG Video Recording API
This is an API which can be used to save video recording, get all videos.
Here is how to use this API
## Upload Video
To upload a video, send a **POST** request to the endpoint `https://hng-video-recording.onrender.com/api/`.
The request body must contain video you want to upload, that is:
| Required Field | Description
| ----------- | ----------- |
| video | Video you want to upload |

Here is an example written in JavaScript (Fetch).
```
var formdata = new FormData();
formdata.append("video", fileInput.files[0], "007 Summary of Beginning to Write.mp4");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://hng-video-recording.onrender.com/api/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Here is what the expected response should look like
```
{
    "pk": 3,
    "video": "https://res.cloudinary.com/dxtugxga0/video/upload/v1/video-recording/media/video/2023-10-01/007_Summary_of_Beginning_to_Write_pt6310",
    "transcription": "okay so we just covered beginning to write and we're almost ready in the next section we're actually going to write so here we talked about the when where and how I hope you have a place of time and you tell everybody to leave you alone during that and keeping a journal it's your choice I recommend it right at any way you can write forget about this course stop this course right now and go right instead I would prefer that choosing the right word we talked about how to do that and standard story arcs and character types and your project is to start a journal it's up to you as to whether you do that or not and next up we're actually going to write oh boy I'm so excited I'll see you there"
}
```
## Get All Uploaded/Saved Videos
To get all uploaded or saved videos, send a **GET** request to the endpoint `https://hng-video-recording.onrender.com/api/`. Here is an example written in JavaScript (Fetch)
```
var formdata = new FormData();

var requestOptions = {
  method: 'GET',
  body: formdata,
  redirect: 'follow'
};

fetch("https://hng-video-recording.onrender.com/api/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Here is how the response should look like
```
[
    {
        "pk": 3,
        "video": "https://res.cloudinary.com/dxtugxga0/video/upload/v1/video-recording/media/video/2023-10-01/007_Summary_of_Beginning_to_Write_pt6310",
        "transcription": "okay so we just covered beginning to write and we're almost ready in the next section we're actually going to write so here we talked about the when where and how I hope you have a place of time and you tell everybody to leave you alone during that and keeping a journal it's your choice I recommend it right at any way you can write forget about this course stop this course right now and go right instead I would prefer that choosing the right word we talked about how to do that and standard story arcs and character types and your project is to start a journal it's up to you as to whether you do that or not and next up we're actually going to write oh boy I'm so excited I'll see you there"
    },
    ...
]
```
## Get An Uploaded Video
To get an uploaded video, send a **GET** request to the endpoint `https://hng-video-recording.onrender.com/api/<video_pk>/`. Replace <video_pk> with the pk (primary key) of the video.
Here is an example written in JavaScript (Fetch)
```
var formdata = new FormData();

var requestOptions = {
  method: 'GET',
  body: formdata,
  redirect: 'follow'
};

fetch("https://hng-video-recording.onrender.com/api/3/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Here is how the response should look like
```
{
    "pk": 3,
    "video": "https://res.cloudinary.com/dxtugxga0/video/upload/v1/video-recording/media/video/2023-10-01/007_Summary_of_Beginning_to_Write_pt6310",
    "transcription": "okay so we just covered beginning to write and we're almost ready in the next section we're actually going to write so here we talked about the when where and how I hope you have a place of time and you tell everybody to leave you alone during that and keeping a journal it's your choice I recommend it right at any way you can write forget about this course stop this course right now and go right instead I would prefer that choosing the right word we talked about how to do that and standard story arcs and character types and your project is to start a journal it's up to you as to whether you do that or not and next up we're actually going to write oh boy I'm so excited I'll see you there"
}
```
