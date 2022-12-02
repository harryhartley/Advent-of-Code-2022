use std::{collections::HashMap};

fn main() {
    let input: &str = include_str!("../input.txt");
    let rps: HashMap<&str, (i32, i32)> = HashMap::from([
        ("A X", (4, 3)), ("A Y", (8, 4)), ("A Z", (3, 8)),
        ("B X", (1, 1)), ("B Y", (5, 5)), ("B Z", (9, 9)),
        ("C X", (7, 2)), ("C Y", (2, 6)), ("C Z", (6, 7)),
    ]);
    println!("Silver: {}", silver(input, &rps));
    println!("Gold: {}", gold(input, &rps));
}

fn silver(input: &str, rps: &HashMap<&str, (i32, i32)>) -> i32 {
    input.split("\n").map(|x: &str| rps[x].0).sum()
}

fn gold(input: &str, rps: &HashMap<&str, (i32, i32)>) -> i32 {
    input.split("\n").map(|x: &str| rps[x].1).sum()
}