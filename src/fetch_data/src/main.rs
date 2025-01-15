use reqwest::Error;
use std::fs::File;
use std::io::Write;
use anyhow::{Context, Result};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let url = "https://jsonplaceholder.typicode.com/posts";
    let response = reqwest::get(url).await?;

    // Ensure the response is valid (status 200)
    if response.status().is_success() {
        let body = response.text().await?;

        // Save data to a file
        let file = File::create("./data.json")
            .context("Failed to create file './data.json'");

        if file.unwrap().write_all(body.as_bytes()).is_err() {
            println!("Failed to write to ./data.json");
        }

        println!("successfully wrote to ./data.json");
    } else {
        println!("Request failed: {}", response.status());
    }

    Ok(())
}
