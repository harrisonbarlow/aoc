use std::fs::File;
use std::collections::HashSet;
use std::io::{self, BufReader, BufRead};

fn read_input(file_name: &str) -> io::Result<BufReader<File>> {
    let file = File::open(file_name)?;
    Ok(BufReader::new(file))
}

fn solve2(input: BufReader<File>) -> i32 {
    let mut sum = 0;
    let mut common = HashSet::new();

    for line in input.lines() {
        if common.len() == 0 {
            for character in line.unwrap().chars() {
                common.insert(character);
            }
        } else {
            
        }
    }
        

    0
}

fn main() {
    let input: BufReader<File> = read_input("input.txt").unwrap();
    
    println!("Part 2: {}", solve2(input));
}