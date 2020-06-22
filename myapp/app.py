#!/usr/bin/env python3

from aws_cdk import core

from webapp.networking_stack import NetworkingStack
from webapp.compute_stack import ComputeStack
from webapp.database_stack import DatabaseStack

app = core.App()

networking = NetworkingStack(app, "networking")
compute = ComputeStack(app, "compute", networking.vpc )
database = DatabaseStack(app, 'database', networking.vpc, compute.asg.connections.security_groups)

app.synth()
