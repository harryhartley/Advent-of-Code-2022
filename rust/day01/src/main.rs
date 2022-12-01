fn main() {
    let input: &str = include_str!("../input.txt");
    println!("Silver: {}", silver(input));
    println!("Gold: {}", gold(input));
}

fn silver(input: &str) -> i32 {
    input
        .split("\n\n")
        .map(|x| x.lines().map(|y| y.parse::<i32>().unwrap()).sum())
        .max()
        .unwrap_or(0)
}

fn gold(input: &str) -> i32 {
    let mut totals: Vec<i32> = input
        .split("\n\n")
        .map(|x| x.lines().map(|y| y.parse::<i32>().unwrap()).sum())
        .collect();
    totals.sort();
    totals.iter().rev().take(3).sum()
}