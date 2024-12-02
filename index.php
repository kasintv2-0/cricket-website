<?php
// Get the 'get' parameter from the query string
$get = $_GET['get']; 

// Define the base URL for the M3U8 stream
$baseUrl = 'https://dai.fancode.com';

// Construct the full URL by appending the 'get' parameter to the base URL
$mpdUrl = $baseUrl . $get;

// Set the request headers
$mpdheads = [
    'http' => [
        'header' => "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0\r\n" .
                   "Referer: https://www.fancode.com/\r\n", // Fancode referrer header
        'follow_location' => 1,
        'timeout' => 5
    ]
];

// Create the context with the headers
$context = stream_context_create($mpdheads);

// Fetch the M3U8 file content from the constructed URL
$res = file_get_contents($mpdUrl, false, $context);

// Check if content was retrieved successfully
if ($res === false) {
    echo "Error: Unable to fetch the content.";
} else {
    echo $res;  // Output the M3U8 content
}
?>
