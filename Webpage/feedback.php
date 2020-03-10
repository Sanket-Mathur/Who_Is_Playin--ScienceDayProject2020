<?php

if(isset($_POST['feed']))
{
    if(isset($_POST['email']))
    {
        $data = $_POST['name'].','.$_POST['email']."\r\n".$_POST['feed']."\r\n\n";
        $ret = file_put_contents('feed.txt', $data, FILE_APPEND);
        if($ret === false)
        {
            die('There was an error writing this file');
        }
        else
        {
            header('Location: index.html');
        }
    }
    else
    {
        $data = "ANONYMOUS"."\r\n".$_POST['feed']."\r\n";
        $ret = file_put_contents('feed.txt', $data, FILE_APPEND);
        if($ret === false)
        {
            die('There was an error writing this file');
        }
        else
        {
            header('Location: index.html');
        }
    }
}
else
{
    die('Sorry, try again!!!');
}

?>