import java.io.*;
import java.net.*;

public class SocketHTTPClient {
    public static void main(String[] args) {
        try {
            // Create a socket to connect to the web server on port 80 (HTTP)
            Socket socket = new Socket("www.martinbroadhurst.com", 80);
            socket.setSoTimeout(5000); // Optional: 5-second timeout

            // Get the output stream to send the request
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Send a valid HTTP GET request
            out.println("GET / HTTP/1.1");
            out.println("Host: www.martinbroadhurst.com");
            out.println("Connection: close"); // Ask server to close connection after response
            out.println(); // Blank line to indicate end of headers

            // Get the input stream to read the response
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Read and print the server's response
            String responseLine;
            while ((responseLine = in.readLine()) != null) {
                System.out.println(responseLine);
            }

            // Close the connections
            in.close();
            out.close();
            socket.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
