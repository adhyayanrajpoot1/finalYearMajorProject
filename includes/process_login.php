<?php


include_once 'db_connect.php';
include_once 'functions.php';

sec_session_start(); // Our custom secure way of starting a PHP session.
//echo("inside isset");
if (isset($_POST['email'], $_POST['p'])) {
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $password = $_POST['p']; // The hashed password.
    echo("<br>HELLO");
    $isLogin = login($email, $password, $mysqli);
    echo(login($email, $password, $mysqli));
    if ($isLogin == true) {
        // Login success 
        echo("inside if");
        header("Location: ../medical/medical-record.php");
        exit();
    } else {
        // Login failed 
        echo("inside else");
        header('Location: ../index.php?error=1');
        exit();
    }
} else {
    // The correct POST variables were not sent to this page. 
    header('Location: ../error.php?err=Could not process login');
    exit();
}
?>