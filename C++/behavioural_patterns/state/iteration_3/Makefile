################################################################################
#
# Makefile for the State design pattern example.
#
# Author: Jeff Shantz
#
# To build, simply type 'make'.
#
################################################################################

BIN=loc

all: $(BIN)

loc: main.o AppliedState.o ApplyCommand.o ApproveCommand.o CancelCommand.o LineOfCredit.o LineOfCreditState.o Menu.o MenuItem.o NewState.o OpenState.o PayCommand.o QuitCommand.o WithdrawCommand.o
	g++ -o $@ $^ $(LFLAGS) $(LIBS)

%.o: %.cpp
	g++ -c $<

clean:
	rm -f *.o *.log $(BIN)

realclean: clean
	rm -f $(BIN)
