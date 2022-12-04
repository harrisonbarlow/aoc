use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut index = 0;

    let mut elves: Vec<u32> = Vec::new();
    elves.push(0);
    
    for line in reader.lines() {
        let current: String = line.unwrap();

        if current == "" {
            index += 1;
            elves.push(0);
        } else {
            let value: u32 = current.parse().unwrap();
            elves[index] += value;  
        }
    }

    elves.sort();
    elves.reverse();

    println!("{}", elves[0]);
    println!("{}", elves.iter().take(3).sum::<u32>());

    Ok(())
}