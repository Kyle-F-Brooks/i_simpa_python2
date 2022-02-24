# i_simpa_python2
These scripts were either written or modified by Kyle Brooks

## Installation
Each folder contains the required files to run the tools within I-Simpa 1.3.4 with the Python 2.x Interperator. 
**Administrator controls are required to install any of these tools**

1. Download the desired tools by pressing the "Code" button at the top of the screen and then "Download ZIP"
2. Open the I-Simpa folder usually located at C:\Program Files\I-SIMPA\UserScript
3. Paste the tool folder into the user script folder **Note:** recp_res_tool goes into the ..\I-SIMPA\SystemScript folder and replaces the one already contained within.
4. Reboot any open instances of I-Simpa 

## all_reciever_tool
This tool is used to enable and disable the name tags on each punctual reciever to make viewing of the model easier.
Directivity Lines can now be hidden but not re-enabled.

## convert_all_tool
An edited version of a script that converts the gabe format files into csv. The changes made, allow it to be used with python 3 as in the latest version of I-Simpa. 

## recp_res_tool
Combines each value of a chosen measurement into a single file to allow for easier processing of data. Each file gets saved in a folder called "Fused Recievers" and the file name is appended with the measurement that was chosen.

## absorption_calc
using the EDT, calculate the sabine and absorption coefficient

## source_contributions
Used to get the specific source contribution for each microphone and output a file for each source with the spl reading at each receiver

## plot_xyz
Used to convert a grid of microphone data into a readable format for plotting libraries such as d-plot, can read the output of the source contributions

## stl_calc
calculates the Transmission loss