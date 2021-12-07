use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut vec: Vec<i32> = Vec::new();
    let mut sliding: Vec<i32> = Vec::new();
    let mut counter: i32 = 0;
    
    for line in reader.lines() {
        let curr_line: i32 = line.unwrap().parse().unwrap();
        vec.push(curr_line)            
    }

    for (i, x) in vec.iter().enumerate() {
        let val: i32;
        if i < vec.len() - 2 {
            let val: i32 = vec[i] + vec[i+1] + vec[i+2];
            sliding.push(val);
        }
    }

    for (i, x) in sliding.iter().enumerate() {
        if i > 0 {
            if x > &sliding[i - 1] {
                counter = counter + 1;
            }
        }
    }

    println!("{}", counter);

    Ok(())
}