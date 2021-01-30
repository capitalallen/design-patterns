#include "Logger.h"

void f(const Logger& log)
{
  log << "In function f()";
}

int main()
{
  Logger log;
  log << "Starting program";

  f(log);
}
