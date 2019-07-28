struct GumballMachine {
    number_of_gumballs: usize,

    sold_out_state: Box<dyn StateChange>,
}

impl GumballMachine {
    fn new(&self, number_of_gumballs: usize) -> GumballMachine {
        GumballMachine {
            number_of_gumballs,
            sold_out_state: Box::new(SoldOutState {gumball_machine: self}),
        }
    }
}

pub trait StateChange {
    fn insert_quarter(&self);
    fn eject_quarter(&self);
    fn turn_crank(&self);
    fn dispense(&self);
}

struct SoldOutState<'a>{
    gumball_machine: &'a GumballMachine,
}


impl StateChange for SoldOutState{
    fn insert_quarter(&self){ println!("inserted quarter") }
    fn eject_quarter(&self){ println!("ejected quarter") }
    fn turn_crank(&self){ println!("turned crank") }
    fn dispense(&self){ println!("dispensed gumball") }
}
