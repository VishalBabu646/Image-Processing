clc;clear all;close all;
u=imread('cameraman.tif');
th = input("Enter the Threshold value : ");
[r0,c0]=size(u);
for i=1:8:r0
for j=1:8:c0
blk=u(i:i+7,j:j+7);
temp=dct2(blk); 
temp(abs(temp)<=th)=0;
g=idct2(temp);
out(i:i+7,j:j+7)=g;
end
end
out=uint8(out);
[s,t] = size(temp);
nz = nnz(temp);
e = s*t;
fprintf("Compression ratio is %d : %d\n",nz,e);
error = zeros(8);
error = abs(u-out);
errms = rms(out);
irms = rms(error);
snr = errms / irms
fprintf(" The Signal To Noise Ratio is : %f\n",snr);
snrt = num2str(snr);
tex = "output_" + snrt + ".png";
imwrite(out,tex);
subplot(1,2,1);
imshow(u);
subplot(1,2,2);
imshow(uint8(out));