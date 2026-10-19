// Cloud command starter (see 27). Registration mirrors the AST; domain logic stays elsewhere.
package com.example.commands;

import org.incendo.cloud.annotations.Argument;
import org.incendo.cloud.annotations.Command;
import org.incendo.cloud.annotations.CommandDescription;
import org.incendo.cloud.annotations.Permission;

public final class ExampleCommands {

    private final ExampleService service;

    public ExampleCommands(ExampleService service) {
        this.service = service;
    }

    @Command("example create <name>")
    @CommandDescription("Create an example resource.")
    @Permission("plugin.example.create")
    public void create(CommandSenderAdapter sender,
                       @Argument(value = "name", suggestions = "exampleNames") String name) {
        // 1. parse/validate (usage errors here, see 08)
        // 2. permission already enforced by @Permission; extra capability checks here
        // 3. delegate: service.create(sender, name) — no domain logic inline
        // 4. present result via locale keys (48), never hardcoded text
    }

    @Command("example remove <name>")
    @CommandDescription("Remove an example resource.")
    @Permission("plugin.example.remove")
    public void remove(CommandSenderAdapter sender,
                       @Argument(value = "name", suggestions = "exampleNames") String name) {
        // destructive leaf: explicit target + confirmation flow first (23/34/49)
    }
}

// Suggestion provider "exampleNames": runtime registry, permission-filtered (11).
// Console support: declare per leaf in the AST (10/24); region-touching effects
// route through the Folia scheduler declared in implementation metadata (45).
