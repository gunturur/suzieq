#!/usr/bin/env python3

# Copyright (c) Dinesh G Dutt
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

import time

from nubia import command, argument

from suzieq.cli.sqcmds.command import SqCommand
from suzieq.sqobjects.tables import TablesObj


@command("tables", help="Information about the various tables")
class TablesCmd(SqCommand):
    def __init__(
        self,
        engine: str = "",
        hostname: str = "",
        start_time: str = "",
        end_time: str = "",
        view: str = "latest",
        datacenter: str = "",
        format: str = "",
        columns: str = "default",
    ) -> None:
        super().__init__(
            engine=engine,
            hostname=hostname,
            start_time=start_time,
            end_time=end_time,
            view=view,
            datacenter=datacenter,
            columns=columns,
            format=format,
            sqobj=TablesObj,
        )

    @command("show")
    def show(self, **kwargs):
        """
        Show Tables
        """
        now = time.time()
        df = self.sqobj.get(hostname=self.hostname, datacenter=self.datacenter)
        self.ctxt.exec_time = "{:5.4f}s".format(time.time() - now)
        return self._gen_output(df)

    @command("describe")
    @argument("table", description="interface name to qualify")
    def summarize(self, table: str = "", **kwargs):
        """
        Summarize fields in table
        """
        now = time.time()
        df = self.sqobj.summarize(table=table)
        self.ctxt.exec_time = "{:5.4f}s".format(time.time() - now)
        return self._gen_output(df)
