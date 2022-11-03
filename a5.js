/*
#Name:         Neha Dedani
#Class:        CS 4720
#Term:         Summer 2022
#Instructor :  Dr. North
Assignment:   Assignment 5
*/

function same()
{
    var checkBoxVal = document.getElementById("sameBox").checked;
    if(checkBoxVal)
    {
        billingName.value = document.getElementById("shippingName").value;
        billingZip.value = document.getElementById("shippingZip").value;
    }
    if(!checkBoxVal)
    {
        billingName.value = "";
        billingZip.value = "";
    }
}