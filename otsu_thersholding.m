% Matlab program to perform Otsu's thresholding 
image=(imread("rice.png")); 
figure(1); 
imshow(image); 
image1=rgb2gray(image); 
[counts,x] = imhist(image1,16); 
thresh= otsuthresh(counts); 
otsu=imbinarize(image1,thresh); 
figure(2); 
imshow(otsu);
