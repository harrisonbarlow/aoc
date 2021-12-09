use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn find_most(mut numbers: Vec<String>) -> String {
    //let most_common = "011101001101";
    let most_common = "10110";

    for (ci, c) in most_common.chars().enumerate() {
        for number in numbers.iter().enumerate() {
            println!("{:?}", number);
        }

        println!("Index is {}, char is {}", ci, c);

        if numbers.len() > 1 {
            numbers.retain( |n| { n.chars().nth(ci).unwrap() == c });
        } else {
            break;
        }
    }

    numbers[0].clone()
}

fn find_least(mut numbers: Vec<String>) -> String {
    let least_common = "100010110010";

    for (ci, c) in least_common.chars().enumerate() {
        if numbers.len() > 1 {
            numbers.retain( |n| { n.chars().nth(ci).unwrap() == c });
        }
    }

    numbers[0].clone()
}

fn solve2(numbers: Vec<String>) {
    let most: String = find_most(numbers.clone());
    println!("{}", most);
    //let least: String = find_least(numbers.clone()); 
    //println!("{}", least);
}

fn gamma(numbers: Vec<String>) {
    let counter = [i32, numbers[0].len()];
    for (index, c) in numbers.iter().enumerate() {

    }
}

fn main() -> io::Result<()> {
    let file = File::open("input2.txt")?;
    let reader = BufReader::new(file);

    let mut numbers: Vec<String> = Vec::new();

    for line in reader.lines() {
        let curr_line: String = line.unwrap();
        numbers.push(curr_line.to_string());
    }

    solve2(numbers);

    Ok(())
}
