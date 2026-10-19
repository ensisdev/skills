package com.example.legacywarps;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

// OBSERVED (simplified from the fixture project)
public final class WarpCommands implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (cmd.getName().equalsIgnoreCase("warp")) {
            Player player = (Player) sender; // ClassCastException from console (OBSERVED RISK)
            if (args.length == 0) return false;
            if (args[0].equals("set")) {
                WarpStore.save(args[1], player.getLocation()); // silent overwrite (OBSERVED RISK)
            } else if (args[0].equals("del")) {
                WarpStore.delete(args[1]); // no confirm, no audit (OBSERVED RISK)
            } else {
                if (!Economy.charge(player, 50)) return true; // silent fail, no message
                Cooldowns.check(player, 10); // silent fail
                player.teleport(WarpStore.get(args[0])); // off-thread unsafe on Folia
            }
            return true;
        }
        if (cmd.getName().equalsIgnoreCase("warplist")) {
            sender.sendMessage(String.join(", ", WarpStore.names())); // no pages, no filter
            return true;
        }
        return false;
    }
}
