<?php

if(isset($_POST['email']))
{
    $data = $_POST['firstname'].'-'.$_POST['lastname'].'-'.$_POST['username'].'-'.$_POST['age'].'-'.$_POST['gender'].'-'.$_POST['email'].'-'.$_POST['mobnumber'].'-'.$_POST['quali'].'-'.$_POST['langs'].'-'.$_POST['city'].'-'.$_POST['state'].'-'.$_POST['country'].'-'.$_POST['password'];
    $ret = file_put_contents('regis.txt', $data, FILE_APPEND);
    if(isset($_POST['alteremail']))
    {
        $data = '-'.$_POST['alteremail'];
        $ret = file_put_contents('regis.txt', $data, FILE_APPEND);
    }
    $data = "\r\n";
    $ret = file_put_contents('regis.txt', $data, FILE_APPEND);
    header('Location: index.html');
}
else
{
    die('Sorry, try again!!!');
}

?>